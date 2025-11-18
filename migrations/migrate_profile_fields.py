#!/usr/bin/env python3
"""
Script de migración idempotente para agregar los campos de perfil
(`username`, `avatar_url`, `bio`) a la tabla `users`.

Uso:
    python migrations/migrate_profile_fields.py
"""

import sys
import os
from typing import Set

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swagger_server.persistence import init_engine


def _get_sqlite_columns(conn) -> Set[str]:
    rows = conn.exec_driver_sql("PRAGMA table_info(users)").fetchall()
    # PRAGMA table_info devuelve: cid, name, type, notnull, dflt_value, pk
    return {row[1] for row in rows}


def migrate():
    print("Iniciando migración de base de datos (perfil de usuario)...")
    engine = init_engine()
    url = str(engine.url)

    with engine.begin() as conn:
        if url.startswith("sqlite"):
            existing = _get_sqlite_columns(conn)

            # username
            if "username" not in existing:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN username VARCHAR(255)")
                print("- Columna 'username' añadida")
            else:
                print("- Columna 'username' ya existe (ok)")

            # avatar_url
            if "avatar_url" not in existing:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN avatar_url VARCHAR(2048)")
                print("- Columna 'avatar_url' añadida")
            else:
                print("- Columna 'avatar_url' ya existe (ok)")

            # bio
            if "bio" not in existing:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN bio VARCHAR(1000)")
                print("- Columna 'bio' añadida")
            else:
                print("- Columna 'bio' ya existe (ok)")

            # Inicializar username con name si está vacío
            conn.exec_driver_sql("UPDATE users SET username = name WHERE username IS NULL")

            # Crear índice único si no existe (SQLite no soporta IF NOT EXISTS en UNIQUE CONSTRAINT)
            # Intentar crear; si existe, ignorar error.
            try:
                conn.exec_driver_sql("CREATE UNIQUE INDEX idx_users_username ON users(username)")
                print("- Índice único 'idx_users_username' creado")
            except Exception:
                print("- Índice único 'idx_users_username' ya existe (ok)")

        else:
            # Fallback genérico (p.ej. PostgreSQL): usar ALTER con IF NOT EXISTS en sentencias separadas
            try:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN IF NOT EXISTS username VARCHAR(255)")
                print("- Columna 'username' verificada/creada")
            except Exception:
                print("- Columna 'username' ya existe o no se pudo verificar (continúa)")
            try:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN IF NOT EXISTS avatar_url VARCHAR(2048)")
                print("- Columna 'avatar_url' verificada/creada")
            except Exception:
                print("- Columna 'avatar_url' ya existe o no se pudo verificar (continúa)")
            try:
                conn.exec_driver_sql("ALTER TABLE users ADD COLUMN IF NOT EXISTS bio VARCHAR(1000)")
                print("- Columna 'bio' verificada/creada")
            except Exception:
                print("- Columna 'bio' ya existe o no se pudo verificar (continúa)")

            conn.exec_driver_sql("UPDATE users SET username = name WHERE username IS NULL")
            try:
                conn.exec_driver_sql("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username ON users(username)")
                print("- Índice único 'idx_users_username' creado/verificado")
            except Exception:
                print("- Índice único 'idx_users_username' ya existe o no se pudo verificar (continúa)")

    print("✅ Migración completada")


if __name__ == "__main__":
    migrate()
