#!/usr/bin/env python3

from __future__ import annotations

import connexion

try:
    from flask_cors import CORS
except ModuleNotFoundError:  # pragma: no cover - fallback when flask-cors missing
    def CORS(app, resources=None):
        @app.after_request
        def add_cors_headers(response):
            response.headers.setdefault("Access-Control-Allow-Origin", "*")
            response.headers.setdefault(
                "Access-Control-Allow-Headers", "Authorization,Content-Type"
            )
            response.headers.setdefault(
                "Access-Control-Allow-Methods", "GET,POST,OPTIONS"
            )
            response.headers.setdefault("Access-Control-Allow-Credentials", "true")
            return response

        return app

from swagger_server import encoder
from swagger_server.config import get_settings
from swagger_server.persistence import Base, Session, init_engine, init_session


def create_app() -> connexion.App:
    settings = get_settings()
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder

    engine = init_engine(settings.db_url)
    init_session(engine)
    Base.metadata.create_all(bind=engine)

    CORS(
        app.app,
        resources={r"/*": {"origins": ["http://localhost:4200", "http://localhost:5173", "*"]}},
    )

    @app.app.teardown_appcontext
    def remove_session(exception=None):  # pragma: no cover - flask teardown
        if Session is not None:
            Session.remove()

    app.add_api(
        "swagger.yaml",
        arguments={"title": "Usuarios y Autorización"},
        pythonic_params=True,
        base_path="/",
    )

    return app


def main():
    app = create_app()
    app.run(port=8080)


if __name__ == "__main__":
    main()
