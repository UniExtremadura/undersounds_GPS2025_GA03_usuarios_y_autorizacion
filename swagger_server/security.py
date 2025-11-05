from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Dict

try:
    import bcrypt  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fallback for offline envs
    from swagger_server import bcrypt_fallback as bcrypt
import jwt
from jwt import InvalidTokenError

from swagger_server import config


def hash_password(password: str) -> str:
    if not password:
        raise ValueError("La contraseña no puede estar vacía")
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    if not password_hash:
        return False
    try:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
    except ValueError:
        return False


def _build_payload(user_id: int, token_type: str, ttl_seconds: int) -> Dict[str, object]:
    now = datetime.now(timezone.utc)
    return {
        "sub": str(user_id),
        "typ": token_type,
        "iat": now,
        "exp": now + timedelta(seconds=ttl_seconds),
    }


def _encode(payload: Dict[str, object]) -> str:
    settings = config.get_settings()
    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")


def issue_tokens(user_id: int) -> Dict[str, str]:
    settings = config.get_settings()
    access_payload = _build_payload(user_id, "access", settings.access_ttl)
    refresh_payload = _build_payload(user_id, "refresh", settings.refresh_ttl)
    return {
        "access": _encode(access_payload),
        "refresh": _encode(refresh_payload),
    }


def decode_token(token: str, expected_type: str | None = None) -> Dict[str, object]:
    settings = config.get_settings()
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=["HS256"],
            options={"require": ["sub", "typ", "iat", "exp"]},
        )
    except InvalidTokenError as exc:  # pragma: no cover - mapping error types
        raise exc

    token_type = payload.get("typ")
    if expected_type and token_type != expected_type:
        raise InvalidTokenError("Tipo de token inválido")

    sub = payload.get("sub")
    try:
        user_id = int(sub)
    except (TypeError, ValueError) as exc:
        raise InvalidTokenError("Identificador de usuario inválido") from exc

    return {"user_id": user_id, "typ": token_type, "payload": payload}
