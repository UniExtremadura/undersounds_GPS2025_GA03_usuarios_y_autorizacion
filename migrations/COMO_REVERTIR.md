# Guía de Reversión de Cambios

## 🔄 CÓMO DESHACER LOS CAMBIOS

Si ejecutaste la migración y quieres revertirla, sigue estos pasos:

### 1️⃣ Revertir Base de Datos

**SQLite:**
```bash
cd undersounds_GPS2025_GA03_usuarios_y_autorizacion
sqlite3 undersounds.db < migrations/rollback_profile_fields.sql
```

**PostgreSQL:**
```bash
psql -d undersounds -f migrations/rollback_profile_fields_postgres.sql
```

### 2️⃣ Revertir Código del Backend

**Git (si hiciste commit):**
```bash
cd undersounds_GPS2025_GA03_usuarios_y_autorizacion
git checkout HEAD -- swagger_server/models_db.py
git checkout HEAD -- swagger_server/controllers/me_controller.py
```

**Manual:**
1. Abre `swagger_server/models_db.py`
2. Elimina las líneas que agregamos:
   - `username = Column(String(255), nullable=True, unique=True, index=True)`
   - `avatar_url = Column(String(2048), nullable=True)`
   - `bio = Column(String(1000), nullable=True)`

3. En el método `to_private_payload()`, cambia:
   ```python
   "username": self.username or self.name,
   "avatarUrl": self.avatar_url,
   "bio": self.bio,
   "createdAt": self.created_at.isoformat() if self.created_at else None,
   ```
   
   Por:
   ```python
   "username": self.name,
   "avatarUrl": None,
   "bio": None,
   ```

4. Abre `swagger_server/controllers/me_controller.py`
5. Cambia la función `me_patch()` por:
   ```python
   def me_patch(body):
       if connexion.request.is_json:
           body = UserUpdate.from_dict(connexion.request.get_json())
       return 'do some magic!'
   ```

### 3️⃣ Revertir Frontend (si quieres)

**Git:**
```bash
cd undersounds_GPS2025_GA03_frontend
git checkout HEAD -- src/app/services/auth.service.ts
git checkout HEAD -- src/app/pages/profile/
```

### 4️⃣ Eliminar Archivos de Migración (opcional)

```bash
cd undersounds_GPS2025_GA03_usuarios_y_autorizacion
rm -rf migrations/
rm ACTUALIZAR_BACKEND.md
rm RESUMEN_CAMBIOS.md
```

---

## ⚠️ IMPORTANTE

- La reversión **eliminará todos los datos** de username, avatar_url y bio que hayas guardado
- Haz backup de la base de datos antes de revertir si tienes datos importantes
- Los usuarios seguirán funcionando normalmente sin estos campos

---

## 💡 ALTERNATIVA: NO EJECUTAR LA MIGRACIÓN

Si no has ejecutado la migración aún, simplemente **no la ejecutes** y los cambios del backend no tendrán efecto. El frontend funcionará pero dará error al intentar actualizar el perfil.

Para usar solo el frontend sin el backend:
1. No ejecutes la migración
2. El perfil se verá bonito pero no guardará cambios
3. Los cambios solo quedarán en el código, no en la BD
