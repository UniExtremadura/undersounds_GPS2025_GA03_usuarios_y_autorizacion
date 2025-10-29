import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.paged_reviews import PagedReviews  # noqa: E501
from swagger_server.models.paged_users import PagedUsers  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.models.reviews_review_id_body import ReviewsReviewIdBody  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.user_admin_update import UserAdminUpdate  # noqa: E501
from swagger_server.models.user_id_roles_body import UserIdRolesBody  # noqa: E501
from swagger_server.models.user_public import UserPublic  # noqa: E501
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


def users_get(q=None, role=None, page=None, page_size=None):  # noqa: E501
    """Listado de usuarios

     # noqa: E501

    :param q: 
    :type q: str
    :param role: 
    :type role: dict | bytes
    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        role = Role.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
