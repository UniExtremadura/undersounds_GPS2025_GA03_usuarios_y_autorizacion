-- Migración para agregar campos de perfil a la tabla users (PostgreSQL)
-- Fecha: 2025-11-18
-- Descripción: Agrega username, avatar_url y bio a la tabla users

-- Agregar columnas
ALTER TABLE users ADD COLUMN IF NOT EXISTS username VARCHAR(255);
ALTER TABLE users ADD COLUMN IF NOT EXISTS avatar_url VARCHAR(2048);
ALTER TABLE users ADD COLUMN IF NOT EXISTS bio VARCHAR(1000);

-- Actualizar username con el valor de name para usuarios existentes
UPDATE users SET username = name WHERE username IS NULL;

-- Agregar constraint de unicidad para username
ALTER TABLE users ADD CONSTRAINT users_username_unique UNIQUE (username);

-- Crear índice para username (si no existe)
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
