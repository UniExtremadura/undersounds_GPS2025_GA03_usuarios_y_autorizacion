"""Minimal bcrypt fallback using PBKDF2.

This is only intended for development environments where the native bcrypt
wheel is unavailable. It does **not** implement the bcrypt algorithm and should
not be used in production.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
from typing import Union

PasswordType = Union[bytes, bytearray, memoryview]


def gensalt(rounds: int = 12) -> bytes:  # pragma: no cover - simple wrapper
    salt = os.urandom(16)
    return base64.b64encode(salt)


def _ensure_bytes(data: Union[str, PasswordType]) -> bytes:
    if isinstance(data, (bytes, bytearray, memoryview)):
        return bytes(data)
    return str(data).encode("utf-8")


def hashpw(password: Union[str, PasswordType], salt: Union[str, bytes]) -> bytes:
    password_bytes = _ensure_bytes(password)
    salt_bytes = base64.b64decode(_ensure_bytes(salt))
    digest = hashlib.pbkdf2_hmac("sha256", password_bytes, salt_bytes, 200_000)
    return base64.b64encode(salt_bytes + digest)


def checkpw(password: Union[str, PasswordType], hashed: Union[str, bytes]) -> bool:
    password_bytes = _ensure_bytes(password)
    hashed_bytes = base64.b64decode(_ensure_bytes(hashed))
    salt = hashed_bytes[:16]
    stored_digest = hashed_bytes[16:]
    new_digest = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, 200_000)
    return hmac.compare_digest(stored_digest, new_digest)
