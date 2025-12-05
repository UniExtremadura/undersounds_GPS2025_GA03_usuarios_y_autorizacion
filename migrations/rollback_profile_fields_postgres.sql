-- Script para REVERTIR la migración de campos de perfil (PostgreSQL)
-- Fecha: 2025-11-18
-- Descripción: Elimina las columnas username, avatar_url y bio de la tabla users

-- ADVERTENCIA: Esto eliminará todos los datos de username, avatar y bio de los usuarios

-- PostgreSQL soporta DROP COLUMN directamente

-- Eliminar constraint de unicidad
ALTER TABLE users DROP CONSTRAINT IF EXISTS users_username_unique;

-- Eliminar índice
DROP INDEX IF EXISTS idx_users_username;

-- Eliminar columnas
ALTER TABLE users DROP COLUMN IF EXISTS username;
ALTER TABLE users DROP COLUMN IF EXISTS avatar_url;
ALTER TABLE users DROP COLUMN IF EXISTS bio;
