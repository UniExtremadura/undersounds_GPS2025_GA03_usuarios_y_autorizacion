from __future__ import annotations

import connexion
import six
from sqlalchemy import func, or_, select

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.paged_reviews import PagedReviews  # noqa: E501
from swagger_server.models.paged_users import PagedUsers  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.models.reviews_review_id_body import ReviewsReviewIdBody  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.user_admin_update import UserAdminUpdate  # noqa: E501
from swagger_server.models.user_id_roles_body import UserIdRolesBody  # noqa: E501
from swagger_server.models.user_public import UserPublic  # noqa: E501
from swagger_server.models_db import RoleEnum, User
from swagger_server.persistence import get_session
from swagger_server import util


def admin_reviews_get(user_id=None, product_id=None, status=None, page=None, page_size=None):  # noqa: E501
    """Moderar reseñas (listar/filtrar)

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :param product_id: 
    :type product_id: str
    :param status: 
    :type status: str
    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: PagedReviews
    """
    return 'do some magic!'


def admin_reviews_review_id_patch(body, review_id):  # noqa: E501
    """Moderar estado de una reseña

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param review_id: 
    :type review_id: str

    :rtype: Review
    """
    if connexion.request.is_json:
        body = ReviewsReviewIdBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def _normalize_role(role_param) -> RoleEnum | None:
    if role_param is None:
        return None
    if isinstance(role_param, dict):  # pragma: no cover - defensive path
        role_param = role_param.get("value") or role_param.get("role")
    if not isinstance(role_param, str):
        return None
    value = role_param.strip().lower()
    if not value:
        return None
    mapping = {
        "listener": RoleEnum.OYENTE,
        "oyente": RoleEnum.OYENTE,
        "artist": RoleEnum.ARTISTA,
        "artista": RoleEnum.ARTISTA,
        "admin": RoleEnum.ADMIN,
    }
    return mapping.get(value)


def users_get(q=None, role=None, page=None, page_size=None, token_info=None):  # noqa: E501
    """Listado de usuarios"""

    info = token_info or connexion.context.get("token_info", {})
    if not info or info.get("typ") != "access":
        return {"mensaje": "No autenticado"}, 401

    session = get_session()
    requester = session.get(User, info.get("user_id"))
    if not requester or requester.role != RoleEnum.ADMIN:
        return {"mensaje": "No autorizado"}, 403

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

    filters = []
    if q:
        term = f"%{q.strip().lower()}%"
        filters.append(
            or_(func.lower(User.name).like(term), func.lower(User.email).like(term))
        )

    role_enum = _normalize_role(role)
    if role and role_enum is None:
        return {"mensaje": "Rol inválido"}, 400
    if role_enum is not None:
        filters.append(User.role == role_enum)

    count_stmt = select(func.count()).select_from(User)
    data_stmt = select(User).order_by(User.id)
    if filters:
        count_stmt = count_stmt.where(*filters)
        data_stmt = data_stmt.where(*filters)

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
                "username": user.name,
                "name": user.name,
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


def users_user_id_followers_get(user_id, page=None, page_size=None):  # noqa: E501
    """Listar seguidores de un usuario (admin o dueño)

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: PagedUsers
    """
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """Detalle de usuario

     # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: UserPublic
    """
    return 'do some magic!'


def users_user_id_patch(body, user_id):  # noqa: E501
    """Edita usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: 
    :type user_id: str

    :rtype: UserPublic
    """
    if connexion.request.is_json:
        body = UserAdminUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_roles_patch(body, user_id):  # noqa: E501
    """Asigna/quita roles

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserIdRolesBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
