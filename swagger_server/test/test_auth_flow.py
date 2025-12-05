import os
import threading
import time

import pytest
import requests
from werkzeug.serving import make_server

from swagger_server import config
from swagger_server.__main__ import create_app


@pytest.fixture(scope="module")
def api_server(tmp_path_factory):
    db_dir = tmp_path_factory.mktemp("db")
    db_path = db_dir / "test.db"
    os.environ["DB_URL"] = f"sqlite:///{db_path}"
    os.environ["JWT_SECRET"] = "test-secret"
    os.environ["ACCESS_TTL"] = "900"
    os.environ["REFRESH_TTL"] = "2592000"
    config.get_settings.cache_clear()

    app = create_app()
    server = make_server("127.0.0.1", 0, app.app)
    port = server.socket.getsockname()[1]

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    time.sleep(0.2)
    yield f"http://127.0.0.1:{port}"

    server.shutdown()
    thread.join(timeout=5)


@pytest.fixture(scope="module")
def register_user(api_server):
    payload = {
        "name": "Ana",
        "username": "Ana",
        "email": "ana@demo.com",
        "password": "Passw0rd!",
        "role": "artist",
    }
    response = requests.post(f"{api_server}/auth/register", json=payload, timeout=5)
    assert response.status_code == 201
    return payload, response.json()


@pytest.fixture(scope="module")
def register_admin(api_server):
    payload = {
        "name": "Admin",
        "username": "Admin",
        "email": "admin@demo.com",
        "password": "Adm1nPass!",
        "role": "admin",
    }
    response = requests.post(f"{api_server}/auth/register", json=payload, timeout=5)
    assert response.status_code == 201
    return payload, response.json()


def test_register_success(register_user):
    payload, response = register_user
    assert response["email"] == payload["email"]
    assert response["role"] == payload["role"]
    assert "tokens" in response
    assert "access" in response["tokens"]
    assert "refresh" in response["tokens"]


def test_register_duplicate_email(api_server, register_user):
    payload, _ = register_user
    response = requests.post(f"{api_server}/auth/register", json=payload, timeout=5)
    assert response.status_code == 400
    assert "Email" in response.json().get("mensaje", "")


def test_login_success(api_server, register_user):
    payload, _ = register_user
    response = requests.post(
        f"{api_server}/auth/login",
        json={"email": payload["email"], "password": payload["password"]},
        timeout=5,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == payload["email"]
    assert "access" in data["tokens"]
    assert "refresh" in data["tokens"]


def test_login_invalid_password(api_server, register_user):
    payload, _ = register_user
    response = requests.post(
        f"{api_server}/auth/login",
        json={"email": payload["email"], "password": "incorrecta"},
        timeout=5,
    )
    assert response.status_code == 401


def test_refresh_and_me_flow(api_server, register_user):
    payload, register_response = register_user
    tokens = register_response["tokens"]

    refresh_response = requests.post(
        f"{api_server}/auth/refresh",
        json={"refresh": tokens["refresh"]},
        timeout=5,
    )
    assert refresh_response.status_code == 200
    refreshed = refresh_response.json()
    assert "access" in refreshed and "refresh" in refreshed

    access_token = refreshed["access"]
    me_response = requests.get(
        f"{api_server}/me",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=5,
    )
    assert me_response.status_code == 200
    me_data = me_response.json()
    assert me_data["email"] == payload["email"]
    assert me_data["role"] == payload["role"]

    unauthorized = requests.get(f"{api_server}/me", timeout=5)
    assert unauthorized.status_code == 401


def test_users_list_requires_admin(api_server, register_user):
    _, response = register_user
    access_token = response["tokens"]["access"]
    result = requests.get(
        f"{api_server}/users",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=5,
    )
    assert result.status_code == 403


def test_users_list_as_admin(api_server, register_user, register_admin):
    user_payload, _ = register_user
    _, admin_response = register_admin
    admin_access = admin_response["tokens"]["access"]

    result = requests.get(
        f"{api_server}/users",
        headers={"Authorization": f"Bearer {admin_access}"},
        timeout=5,
    )
    assert result.status_code == 200
    data = result.json()
    assert data["total"] >= 2
    emails = [item["email"] for item in data["items"]]
    assert user_payload["email"] in emails
