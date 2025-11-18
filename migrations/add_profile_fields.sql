-- Migración para agregar campos de perfil a la tabla users
-- Fecha: 2025-11-18
-- Descripción: Agrega username, avatar_url y bio a la tabla users

-- SQLite no permite agregar columnas con UNIQUE directamente, se hace en dos pasos
ALTER TABLE users ADD COLUMN username VARCHAR(255);
ALTER TABLE users ADD COLUMN avatar_url VARCHAR(2048);
ALTER TABLE users ADD COLUMN bio VARCHAR(1000);

-- Actualizar username con el valor de name para usuarios existentes
UPDATE users SET username = name WHERE username IS NULL;

-- Crear índice único para username
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username ON users(username);
