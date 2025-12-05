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
    username = Column(String(255), nullable=True, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum, name="role_enum"), nullable=False)
    avatar_url = Column(String(2048), nullable=True)  # Para URLs largas (base64)
    bio = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_private_payload(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username or self.name,
            "email": self.email,
            "emailVerified": False,
            "role": self.role.value,
            "avatarUrl": self.avatar_url,
            "bio": self.bio,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
        }
