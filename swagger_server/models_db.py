from __future__ import annotations

import enum
from sqlalchemy import Column, DateTime, Enum, Integer, String, func

from swagger_server.persistence import Base


class RoleEnum(str, enum.Enum):
    ARTISTA = "artista"
    OYENTE = "oyente"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum, name="role_enum"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_private_payload(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "username": self.name,
            "email": self.email,
            "emailVerified": False,
            "role": self.role.value,
            "avatarUrl": None,
            "bio": None,
        }
