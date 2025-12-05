from __future__ import annotations

from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from swagger_server.config import get_settings

engine = None
Session: Optional[scoped_session] = None
Base = declarative_base()


def init_engine(db_url: Optional[str] = None):
    """Initialise the SQLAlchemy engine."""
    global engine
    if engine is not None:
        return engine
    url = db_url or get_settings().db_url
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    engine_obj = create_engine(url, future=True, echo=False, connect_args=connect_args)
    engine = engine_obj
    return engine


def init_session(bind_engine=None):
    """Initialise the scoped session factory."""
    global Session
    if Session is not None:
        return Session
    bind = bind_engine or init_engine()
    Session = scoped_session(
        sessionmaker(bind=bind, autocommit=False, autoflush=False, future=True)
    )
    return Session


def get_session():
    """Return a new SQLAlchemy session."""
    if Session is None:
        raise RuntimeError("La sesión de base de datos no está inicializada")
    return Session()
