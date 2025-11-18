from swagger_server.persistence import get_session
from sqlalchemy import func, or_, select
from swagger_server.models_db import User, RoleEnum

def artists_get(page=None, page_size=None, q=None, sort_by=None, sort_order=None, sortBy=None, sortOrder=None, token_info=None): 
    """Listado de artistas con ordenación opcional.

    Parametros:
        sort_by: name | createdAt
        sort_order: asc | desc
    """

    session = get_session()
    try:
        # Paginación segura
        try:
            page_value = int(page) if page is not None else 1
        except (TypeError, ValueError):
            page_value = 1
        page_value = max(page_value, 1)

        try:
            page_size_value = int(page_size) if page_size is not None else 20
        except (TypeError, ValueError):
            page_size_value = 20
        page_size_value = min(max(page_size_value, 1), 100)

        # Filtrado base (solo artistas)
        filters = [User.role == RoleEnum.ARTISTA]

        if q:
            term = f"%{q.strip().lower()}%"
            filters.append(
                or_(func.lower(User.name).like(term), func.lower(User.email).like(term))
            )

        # Ordenación
        # Permitir tanto snake_case como camelCase desde el spec
        sort_by_value = sort_by if sort_by is not None else sortBy
        sort_order_value = sort_order if sort_order is not None else sortOrder

        sort_by_normalized = (sort_by_value or "name").strip()
        sort_order_normalized = (sort_order_value or "asc").strip().lower()

        if sort_by_normalized == "createdAt":
            order_column = User.created_at
        elif sort_by_normalized == "name":
            # lower para orden consistente independiente de mayúsculas
            order_column = func.lower(User.name)
        else:
            # Fallback determinista
            order_column = User.id

        if sort_order_normalized == "desc":
            order_clause = order_column.desc()
        else:
            order_clause = order_column.asc()

        count_stmt = select(func.count()).select_from(User).where(*filters)
        data_stmt = select(User).where(*filters).order_by(order_clause, User.id.asc())

        total = session.execute(count_stmt).scalar_one()
        offset = (page_value - 1) * page_size_value
        rows = (
            session.execute(data_stmt.offset(offset).limit(page_size_value)).scalars().all()
        )

        items = []
        for user in rows:
            created_at = user.created_at.isoformat() if user.created_at else None
            items.append(
                {
                    "id": str(user.id),
                    "name": user.name,
                    "username": user.name,
                    "email": user.email,
                    "role": user.role.value,
                    "createdAt": created_at,
                    "avatarUrl": None,
                    "bio": None,
                }
            )

        payload = {
            "items": items,
            "page": page_value,
            "pageSize": page_size_value,
            "total": total,
            "sortBy": sort_by_normalized,
            "sortOrder": sort_order_normalized,
        }
        return payload, 200
    finally:
        session.close()