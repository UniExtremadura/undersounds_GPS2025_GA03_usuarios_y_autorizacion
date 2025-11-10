from swagger_server.persistence import get_session
from sqlalchemy import func, or_, select
from swagger_server.models_db import User, RoleEnum

def artists_get(page=None, page_size=None, q=None, token_info=None): 
    """ Listado de artistas """

    session = get_session()

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

    # Filtrado

    filters = [User.role == RoleEnum.ARTISTA]

    if q:
        term = f"%{q.strip().lower()}%"
        filters.append(
            or_(func.lower(User.name).like(term), func.lower(User.email).like(term))
        )

    count_stmt = select(func.count()).select_from(User).where(*filters)
    data_stmt = select(User).where(*filters).order_by(User.id)

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
    }
    return payload, 200