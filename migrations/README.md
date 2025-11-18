# Migraciones de Base de Datos

Este directorio contiene las migraciones de la base de datos para el servicio de usuarios y autorización.

## Migración: Campos de Perfil (2025-11-18)

### Descripción
Agrega campos adicionales al perfil de usuario:
- `username`: Nombre de usuario único
- `avatar_url`: URL de la imagen de perfil (soporta base64/Data URLs hasta 2048 caracteres)
- `bio`: Biografía del usuario (hasta 1000 caracteres)

### Ejecución

#### Opción 1: Script Python (Recomendado)
```bash
cd undersounds_GPS2025_GA03_usuarios_y_autorizacion
python migrations/migrate_profile_fields.py
```

Este script utiliza SQLAlchemy para crear/actualizar las tablas automáticamente.

#### Opción 2: SQL Manual (Solo si es necesario)
```bash
# Para SQLite
sqlite3 undersounds.db < migrations/add_profile_fields.sql

# Para PostgreSQL
psql -d undersounds -f migrations/add_profile_fields_postgres.sql
```

### Verificación

Después de ejecutar la migración, puedes verificar que las columnas se agregaron correctamente:

**SQLite:**
```bash
sqlite3 undersounds.db
.schema users
```

**PostgreSQL:**
```sql
\d users
```

Deberías ver las nuevas columnas: `username`, `avatar_url` y `bio`.

### Cambios en el Backend

1. **models_db.py**: Se agregaron las columnas al modelo `User`
2. **me_controller.py**: Se implementó la función `me_patch()` para actualizar el perfil
3. **Endpoint**: `PATCH /me` ahora acepta `username`, `avatarUrl` y `bio`

### Notas Importantes

- El campo `username` es único, la API retornará error 400 si se intenta usar un username ya existente
- El campo `avatar_url` acepta URLs largas (hasta 2048 caracteres) para soportar imágenes en base64
- El campo `bio` tiene un límite de 1000 caracteres
- Para usuarios existentes, el `username` se inicializa con el valor de `name`
