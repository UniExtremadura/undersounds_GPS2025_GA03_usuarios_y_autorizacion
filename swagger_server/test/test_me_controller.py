# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestMeController(BaseTestCase):
    """MeController integration test stubs"""

    def test_me_artist_get(self):
        """Test case for me_artist_get

        Ver mi perfil de artista
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/artist',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_artist_patch(self):
        """Test case for me_artist_patch

        Actualizar perfil de artista (solo role=artist)
        """
        body = ArtistProfileUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/artist',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_consents_get(self):
        """Test case for me_consents_get

        Ver consentimientos de privacidad y marketing
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/consents',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_consents_patch(self):
        """Test case for me_consents_patch

        Actualizar consentimientos
        """
        body = ConsentsUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/consents',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_follows_get(self):
        """Test case for me_follows_get

        Listar a quién sigo
        """
        query_string = [('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/follows',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_follows_post(self):
        """Test case for me_follows_post

        Seguir a un usuario
        """
        body = MeFollowsBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/follows',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_follows_user_id_delete(self):
        """Test case for me_follows_user_id_delete

        Dejar de seguir a un usuario
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/follows/{userId}'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_get(self):
        """Test case for me_get

        Perfil del usuario autenticado
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_password_patch(self):
        """Test case for me_password_patch

        Cambia contraseña autenticado
        """
        body = MePasswordBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/password',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_patch(self):
        """Test case for me_patch

        Actualiza perfil propio
        """
        body = UserUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_get(self):
        """Test case for me_playlists_get

        Listar mis playlists
        """
        query_string = [('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_delete(self):
        """Test case for me_playlists_playlist_id_delete

        Borrar playlist
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}'.format(playlist_id='playlist_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_get(self):
        """Test case for me_playlists_playlist_id_get

        Ver playlist propia
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}'.format(playlist_id='playlist_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_items_get(self):
        """Test case for me_playlists_playlist_id_items_get

        Listar canciones de la playlist
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}/items'.format(playlist_id='playlist_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_items_item_id_delete(self):
        """Test case for me_playlists_playlist_id_items_item_id_delete

        Quitar ítem de la playlist
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}/items/{itemId}'.format(playlist_id='playlist_id_example', item_id='item_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_items_post(self):
        """Test case for me_playlists_playlist_id_items_post

        Añadir canción a la playlist
        """
        body = PlaylistIdItemsBody1()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}/items'.format(playlist_id='playlist_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_items_put(self):
        """Test case for me_playlists_playlist_id_items_put

        Reordenar ítems de la playlist
        """
        body = PlaylistIdItemsBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}/items'.format(playlist_id='playlist_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_patch(self):
        """Test case for me_playlists_playlist_id_patch

        Editar metadatos de playlist
        """
        body = PlaylistUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}'.format(playlist_id='playlist_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_playlist_id_share_post(self):
        """Test case for me_playlists_playlist_id_share_post

        Configurar compartición/visibilidad de playlist
        """
        body = PlaylistShare()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists/{playlistId}/share'.format(playlist_id='playlist_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_playlists_post(self):
        """Test case for me_playlists_post

        Crear playlist
        """
        body = PlaylistCreate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/playlists',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_reviews_get(self):
        """Test case for me_reviews_get

        Mis reseñas de compras
        """
        query_string = [('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/reviews',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_reviews_post(self):
        """Test case for me_reviews_post

        Crear reseña (solo artículos comprados)
        """
        body = ReviewCreate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/reviews',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_reviews_review_id_delete(self):
        """Test case for me_reviews_review_id_delete

        Borrar reseña propia
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/reviews/{reviewId}'.format(review_id='review_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_reviews_review_id_patch(self):
        """Test case for me_reviews_review_id_patch

        Editar reseña propia
        """
        body = ReviewUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/reviews/{reviewId}'.format(review_id='review_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_sessions_get(self):
        """Test case for me_sessions_get

        Lista dispositivos/sesiones activas
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/sessions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_me_sessions_session_id_delete(self):
        """Test case for me_sessions_session_id_delete

        Cierra una sesión concreta
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/me/sessions/{sessionId}'.format(session_id='session_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
