# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.paged_reviews import PagedReviews  # noqa: E501
from swagger_server.models.paged_users import PagedUsers  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.models.reviews_review_id_body import ReviewsReviewIdBody  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.user_admin_update import UserAdminUpdate  # noqa: E501
from swagger_server.models.user_id_roles_body import UserIdRolesBody  # noqa: E501
from swagger_server.models.user_public import UserPublic  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersAdminController(BaseTestCase):
    """UsersAdminController integration test stubs"""

    def test_admin_reviews_get(self):
        """Test case for admin_reviews_get

        Moderar reseñas (listar/filtrar)
        """
        query_string = [('user_id', 'user_id_example'),
                        ('product_id', 'product_id_example'),
                        ('status', 'status_example'),
                        ('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/admin/reviews',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_reviews_review_id_patch(self):
        """Test case for admin_reviews_review_id_patch

        Moderar estado de una reseña
        """
        body = ReviewsReviewIdBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/admin/reviews/{reviewId}'.format(review_id='review_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Listado de usuarios
        """
        query_string = [('q', 'q_example'),
                        ('role', Role()),
                        ('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_followers_get(self):
        """Test case for users_user_id_followers_get

        Listar seguidores de un usuario (admin o dueño)
        """
        query_string = [('page', 2),
                        ('page_size', 100)]
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/users/{userId}/followers'.format(user_id='user_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Detalle de usuario
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/users/{userId}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_patch(self):
        """Test case for users_user_id_patch

        Edita usuario
        """
        body = UserAdminUpdate()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/users/{userId}'.format(user_id='user_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_roles_patch(self):
        """Test case for users_user_id_roles_patch

        Asigna/quita roles
        """
        body = UserIdRolesBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/users/{userId}/roles'.format(user_id='user_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
