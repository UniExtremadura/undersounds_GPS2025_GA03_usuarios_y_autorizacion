"""Funciones auxiliares para la autorización Bearer."""

from jwt import InvalidTokenError

from swagger_server.security import decode_token


def check_bearerAuth(token):
    """Valida un token Bearer JWT."""
    if not token:
        return None
    try:
        token_data = decode_token(token)
    except InvalidTokenError:
        return None
    return {"user_id": token_data["user_id"], "typ": token_data["typ"]}


