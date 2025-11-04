import connexion
import six

from swagger_server.models_db import User
from swagger_server.persistence import get_session

from swagger_server.models.artist_profile import ArtistProfile  # noqa: E501
from swagger_server.models.artist_profile_update import ArtistProfileUpdate  # noqa: E501
from swagger_server.models.consents import Consents  # noqa: E501
from swagger_server.models.consents_update import ConsentsUpdate  # noqa: E501
from swagger_server.models.me_follows_body import MeFollowsBody  # noqa: E501
from swagger_server.models.me_password_body import MePasswordBody  # noqa: E501
from swagger_server.models.paged_playlists import PagedPlaylists  # noqa: E501
from swagger_server.models.paged_reviews import PagedReviews  # noqa: E501
from swagger_server.models.paged_users import PagedUsers  # noqa: E501
from swagger_server.models.playlist import Playlist  # noqa: E501
from swagger_server.models.playlist_create import PlaylistCreate  # noqa: E501
from swagger_server.models.playlist_id_items_body import PlaylistIdItemsBody  # noqa: E501
from swagger_server.models.playlist_id_items_body1 import PlaylistIdItemsBody1  # noqa: E501
from swagger_server.models.playlist_item import PlaylistItem  # noqa: E501
from swagger_server.models.playlist_share import PlaylistShare  # noqa: E501
from swagger_server.models.playlist_update import PlaylistUpdate  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.models.review_create import ReviewCreate  # noqa: E501
from swagger_server.models.review_update import ReviewUpdate  # noqa: E501
from swagger_server.models.session import Session  # noqa: E501
from swagger_server.models.user_private import UserPrivate  # noqa: E501
from swagger_server.models.user_update import UserUpdate  # noqa: E501
from swagger_server import util


def me_artist_get():  # noqa: E501
    """Ver mi perfil de artista

     # noqa: E501


    :rtype: ArtistProfile
    """
    return 'do some magic!'


def me_artist_patch(body):  # noqa: E501
    """Actualizar perfil de artista (solo role&#x3D;artist)

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ArtistProfile
    """
    if connexion.request.is_json:
        body = ArtistProfileUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_consents_get():  # noqa: E501
    """Ver consentimientos de privacidad y marketing

     # noqa: E501


    :rtype: Consents
    """
    return 'do some magic!'


def me_consents_patch(body):  # noqa: E501
    """Actualizar consentimientos

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Consents
    """
    if connexion.request.is_json:
        body = ConsentsUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_follows_get(page=None, page_size=None):  # noqa: E501
    """Listar a quién sigo

     # noqa: E501

    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: PagedUsers
    """
    return 'do some magic!'


def me_follows_post(body):  # noqa: E501
    """Seguir a un usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MeFollowsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_follows_user_id_delete(user_id):  # noqa: E501
    """Dejar de seguir a un usuario

     # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def me_get(token_info=None):  # noqa: E501
    """Perfil del usuario autenticado"""

    info = token_info or connexion.context.get("token_info", {})
    if not info or info.get("typ") != "access":
        return {"mensaje": "No autenticado"}, 401

    session = get_session()
    user = session.get(User, info.get("user_id"))
    if not user:
        return {"mensaje": "Usuario no encontrado"}, 401

    payload = user.to_private_payload()
    payload.update({"name": user.name})
    return payload, 200


def me_password_patch(body):  # noqa: E501
    """Cambia contraseña autenticado

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MePasswordBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_patch(body):  # noqa: E501
    """Actualiza perfil propio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UserPrivate
    """
    if connexion.request.is_json:
        body = UserUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_playlists_get(page=None, page_size=None):  # noqa: E501
    """Listar mis playlists

     # noqa: E501

    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: PagedPlaylists
    """
    return 'do some magic!'


def me_playlists_playlist_id_delete(playlist_id):  # noqa: E501
    """Borrar playlist

     # noqa: E501

    :param playlist_id: 
    :type playlist_id: str

    :rtype: None
    """
    return 'do some magic!'


def me_playlists_playlist_id_get(playlist_id):  # noqa: E501
    """Ver playlist propia

     # noqa: E501

    :param playlist_id: 
    :type playlist_id: str

    :rtype: Playlist
    """
    return 'do some magic!'


def me_playlists_playlist_id_items_get(playlist_id):  # noqa: E501
    """Listar canciones de la playlist

     # noqa: E501

    :param playlist_id: 
    :type playlist_id: str

    :rtype: List[PlaylistItem]
    """
    return 'do some magic!'


def me_playlists_playlist_id_items_item_id_delete(playlist_id, item_id):  # noqa: E501
    """Quitar ítem de la playlist

     # noqa: E501

    :param playlist_id: 
    :type playlist_id: str
    :param item_id: 
    :type item_id: str

    :rtype: None
    """
    return 'do some magic!'


def me_playlists_playlist_id_items_post(body, playlist_id):  # noqa: E501
    """Añadir canción a la playlist

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param playlist_id: 
    :type playlist_id: str

    :rtype: PlaylistItem
    """
    if connexion.request.is_json:
        body = PlaylistIdItemsBody1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_playlists_playlist_id_items_put(body, playlist_id):  # noqa: E501
    """Reordenar ítems de la playlist

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param playlist_id: 
    :type playlist_id: str

    :rtype: List[PlaylistItem]
    """
    if connexion.request.is_json:
        body = PlaylistIdItemsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_playlists_playlist_id_patch(body, playlist_id):  # noqa: E501
    """Editar metadatos de playlist

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param playlist_id: 
    :type playlist_id: str

    :rtype: Playlist
    """
    if connexion.request.is_json:
        body = PlaylistUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_playlists_playlist_id_share_post(body, playlist_id):  # noqa: E501
    """Configurar compartición/visibilidad de playlist

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param playlist_id: 
    :type playlist_id: str

    :rtype: Playlist
    """
    if connexion.request.is_json:
        body = PlaylistShare.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_playlists_post(body):  # noqa: E501
    """Crear playlist

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Playlist
    """
    if connexion.request.is_json:
        body = PlaylistCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_reviews_get(page=None, page_size=None):  # noqa: E501
    """Mis reseñas de compras

     # noqa: E501

    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    :rtype: PagedReviews
    """
    return 'do some magic!'


def me_reviews_post(body):  # noqa: E501
    """Crear reseña (solo artículos comprados)

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Review
    """
    if connexion.request.is_json:
        body = ReviewCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_reviews_review_id_delete(review_id):  # noqa: E501
    """Borrar reseña propia

     # noqa: E501

    :param review_id: 
    :type review_id: str

    :rtype: None
    """
    return 'do some magic!'


def me_reviews_review_id_patch(body, review_id):  # noqa: E501
    """Editar reseña propia

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param review_id: 
    :type review_id: str

    :rtype: Review
    """
    if connexion.request.is_json:
        body = ReviewUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def me_sessions_get():  # noqa: E501
    """Lista dispositivos/sesiones activas

     # noqa: E501


    :rtype: List[Session]
    """
    return 'do some magic!'


def me_sessions_session_id_delete(session_id):  # noqa: E501
    """Cierra una sesión concreta

     # noqa: E501

    :param session_id: 
    :type session_id: str

    :rtype: None
    """
    return 'do some magic!'
