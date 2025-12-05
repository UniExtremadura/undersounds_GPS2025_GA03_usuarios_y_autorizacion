-- Script para REVERTIR la migración de campos de perfil
-- Fecha: 2025-11-18
-- Descripción: Elimina las columnas username, avatar_url y bio de la tabla users

-- ADVERTENCIA: Esto eliminará todos los datos de username, avatar y bio de los usuarios

-- SQLite: Eliminar columnas (SQLite no soporta DROP COLUMN directamente)
-- Necesitarás recrear la tabla

-- PASO 1: Crear tabla temporal con la estructura antigua
CREATE TABLE users_backup (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- PASO 2: Copiar datos (sin los campos nuevos)
INSERT INTO users_backup (id, name, email, password_hash, role, created_at)
SELECT id, name, email, password_hash, role, created_at FROM users;

-- PASO 3: Eliminar tabla original
DROP TABLE users;

-- PASO 4: Renombrar backup a users
ALTER TABLE users_backup RENAME TO users;

-- PASO 5: Recrear índices
CREATE UNIQUE INDEX idx_users_email ON users(email);
