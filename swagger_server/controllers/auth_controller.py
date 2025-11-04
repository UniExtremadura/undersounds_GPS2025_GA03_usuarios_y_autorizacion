from __future__ import annotations

import connexion
from jwt import InvalidTokenError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from swagger_server.models.auth_refresh_body import AuthRefreshBody  # noqa: E501
from swagger_server.models.auth_response import AuthResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.register_request import RegisterRequest  # noqa: E501
from swagger_server.models.reset_confirm_body import ResetConfirmBody  # noqa: E501
from swagger_server.models.reset_request_body import ResetRequestBody  # noqa: E501
from swagger_server.models.token_pair import TokenPair  # noqa: E501
from swagger_server.models.verifyemail_confirm_body import VerifyemailConfirmBody  # noqa: E501
from swagger_server.models.verifyemail_request_body import VerifyemailRequestBody  # noqa: E501
from swagger_server.models_db import RoleEnum, User
from swagger_server.persistence import get_session
from swagger_server.security import decode_token, hash_password, issue_tokens, verify_password


def _token_payload(tokens: dict) -> dict:
    return {
        "access": tokens["access"],
        "refresh": tokens["refresh"],
        "accessToken": tokens["access"],
        "refreshToken": tokens["refresh"],
    }


def _auth_response(user: User, tokens: dict) -> dict:
    payload = {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role.value,
        "user": user.to_private_payload(),
        "tokens": _token_payload(tokens),
    }
    return payload


def _normalize_email(email: str | None) -> str | None:
    if email is None:
        return None
    return email.strip().lower()


def _parse_json(expected_class, default: dict | None = None):
    if connexion.request.is_json:
        raw = connexion.request.get_json()
        if isinstance(raw, dict):
            return raw
        return expected_class.from_dict(raw).to_dict()  # pragma: no cover - fallback
    return default or {}


def auth_login_post(body):  # noqa: E501
    """Inicia sesión"""

    data = _parse_json(LoginRequest, {})
    email = _normalize_email(data.get("email"))
    password = data.get("password")
    if not email or not password:
        return {"mensaje": "Email y contraseña son obligatorios"}, 400

    session = get_session()
    user = session.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not user or not verify_password(password, user.password_hash):
        return {"mensaje": "Credenciales inválidas"}, 401

    tokens = issue_tokens(user.id)
    return _auth_response(user, tokens), 200


def auth_logout_post():  # noqa: E501
    """Cierra sesión actual

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def auth_password_reset_confirm_post(body):  # noqa: E501
    """Confirma nuevo password

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResetConfirmBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_password_reset_request_post(body):  # noqa: E501
    """Solicita reset de contraseña

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResetRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_refresh_post(body):  # noqa: E501
    """Renueva access token con refresh token"""

    data = _parse_json(AuthRefreshBody, {})
    refresh_token = (
        data.get("refresh")
        or data.get("refreshToken")
        or data.get("refresh_token")
    )
    if not refresh_token:
        return {"mensaje": "Refresh token requerido"}, 400

    try:
        token_data = decode_token(refresh_token, expected_type="refresh")
    except InvalidTokenError:
        return {"mensaje": "Token inválido"}, 401

    session = get_session()
    user = session.get(User, token_data["user_id"])
    if not user:
        return {"mensaje": "Usuario no encontrado"}, 401

    tokens = issue_tokens(user.id)
    return _token_payload(tokens), 200


def auth_register_post(body):  # noqa: E501
    """Alta de cuenta"""

    data = _parse_json(RegisterRequest, {})
    name = (data.get("name") or "").strip()
    email = _normalize_email(data.get("email"))
    password = data.get("password")
    role_value = data.get("role")

    if not name or not email or not password or not role_value:
        return {"mensaje": "Todos los campos son obligatorios"}, 400
    if len(password) < 8:
        return {"mensaje": "La contraseña debe tener al menos 8 caracteres"}, 400
    try:
        role = RoleEnum(role_value)
    except ValueError:
        return {"mensaje": "Rol inválido"}, 400

    session = get_session()
    existing = session.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if existing:
        return {"mensaje": "Email ya registrado"}, 400

    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        role=role,
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        return {"mensaje": "Email ya registrado"}, 400
    session.refresh(user)

    tokens = issue_tokens(user.id)
    return _auth_response(user, tokens), 201


def auth_verify_email_confirm_post(body):  # noqa: E501
    """Confirma verificación de email

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VerifyemailConfirmBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_verify_email_request_post(body):  # noqa: E501
    """Envía email de verificación

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VerifyemailRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
