# Instrucciones para Actualizar el Backend

## ⚠️ CAMBIOS REALIZADOS

Se han implementado los siguientes cambios en el backend para soportar la actualización de perfil:

### 1. Modelo de Base de Datos (`models_db.py`)
✅ **Modificado** - Se agregaron 3 nuevas columnas a la clase `User`:
- `username` (VARCHAR(255), UNIQUE, INDEX) - Nombre de usuario único
- `avatar_url` (VARCHAR(2048)) - URL de avatar (soporta base64)
- `bio` (VARCHAR(1000)) - Biografía del usuario

✅ **Modificado** - Se actualizó el método `to_private_payload()` para incluir los nuevos campos

### 2. Controlador (`controllers/me_controller.py`)
✅ **Implementado** - La función `me_patch()` ahora está completamente funcional:
- Valida autenticación del usuario
- Actualiza `username` (con validación de unicidad)
- Actualiza `avatar_url`
- Actualiza `bio`
- Retorna el perfil actualizado

### 3. Migraciones de Base de Datos
✅ **Creado** - Scripts de migración en la carpeta `/migrations/`:
- `add_profile_fields.sql` - Para SQLite
- `add_profile_fields_postgres.sql` - Para PostgreSQL
- `migrate_profile_fields.py` - Script Python automático
- `README.md` - Documentación de migraciones

---

## 🚀 PASOS PARA APLICAR LOS CAMBIOS

### Paso 1: Ejecutar la Migración de Base de Datos

**Opción A - Script Python (RECOMENDADO):**
```bash
cd undersounds_GPS2025_GA03_usuarios_y_autorizacion
python migrations/migrate_profile_fields.py
```

**Opción B - SQL Manual (SQLite):**
```bash
sqlite3 undersounds.db < migrations/add_profile_fields.sql
```

**Opción C - SQL Manual (PostgreSQL):**
```bash
psql -d undersounds -f migrations/add_profile_fields_postgres.sql
```

### Paso 2: Reiniciar el Servidor Backend

```bash
# Detener el servidor si está corriendo
# Ctrl+C

# Iniciar nuevamente
python -m swagger_server
```

### Paso 3: Verificar que Funciona

**Probar con curl:**
```bash
# 1. Login para obtener token
curl -X POST http://localhost:8080/auth/login \
  -H "Content-Type: application/json" \
  -d '{"emailOrUsername":"tu@email.com","password":"tupassword"}'

# 2. Actualizar perfil
curl -X PATCH http://localhost:8080/me \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TU_ACCESS_TOKEN" \
  -d '{
    "username": "nuevo_username",
    "bio": "Mi nueva biografía",
    "avatarUrl": "https://ejemplo.com/avatar.jpg"
  }'

# 3. Obtener perfil actualizado
curl -X GET http://localhost:8080/me \
  -H "Authorization: Bearer TU_ACCESS_TOKEN"
```

---

## 📋 VERIFICACIÓN

Después de aplicar los cambios, verifica:

1. ✅ La base de datos tiene las nuevas columnas:
   ```bash
   sqlite3 undersounds.db ".schema users"
   # Debes ver: username, avatar_url, bio
   ```

2. ✅ El endpoint PATCH /me funciona correctamente

3. ✅ El frontend puede actualizar el perfil sin errores

---

## 🔍 CAMBIOS EN DETALLE

### models_db.py - ANTES:
```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum, name="role_enum"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

### models_db.py - DESPUÉS:
```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=True, unique=True, index=True)  # ✅ NUEVO
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum, name="role_enum"), nullable=False)
    avatar_url = Column(String(2048), nullable=True)  # ✅ NUEVO
    bio = Column(String(1000), nullable=True)  # ✅ NUEVO
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

### me_controller.py - ANTES:
```python
def me_patch(body):
    if connexion.request.is_json:
        body = UserUpdate.from_dict(connexion.request.get_json())
    return 'do some magic!'  # ❌ NO IMPLEMENTADO
```

### me_controller.py - DESPUÉS:
```python
def me_patch(body, token_info=None):
    # ✅ TOTALMENTE IMPLEMENTADO
    # - Valida autenticación
    # - Verifica usuario existe
    # - Valida username único
    # - Actualiza campos
    # - Guarda en BD
    # - Retorna perfil actualizado
```

---

## ⚠️ NOTAS IMPORTANTES

1. **Base64 en avatarUrl**: El campo `avatar_url` tiene 2048 caracteres para soportar imágenes pequeñas en base64. Para imágenes más grandes, considera usar un servicio de almacenamiento externo.

2. **Username único**: Si un usuario intenta usar un `username` que ya existe, la API retornará error 400 con el mensaje "El nombre de usuario ya está en uso".

3. **Usuarios existentes**: La migración automáticamente asigna `username = name` para usuarios existentes.

4. **Compatibilidad**: Los cambios son retrocompatibles. Los usuarios antiguos seguirán funcionando normalmente.

---

## 🐛 TROUBLESHOOTING

**Error: "column username already exists"**
- La migración ya se ejecutó. No hacer nada.

**Error: "no such table: users"**
- Ejecutar primero la inicialización de la base de datos.

**Error: "UNIQUE constraint failed: users.username"**
- El username ya está en uso. Elegir otro nombre de usuario.

**Error: "La sesión de base de datos no está inicializada"**
- Reiniciar el servidor backend.
