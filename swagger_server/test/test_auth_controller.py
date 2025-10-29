# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.auth_refresh_body import AuthRefreshBody  # noqa: E501
from swagger_server.models.auth_response import AuthResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.register_request import RegisterRequest  # noqa: E501
from swagger_server.models.reset_confirm_body import ResetConfirmBody  # noqa: E501
from swagger_server.models.reset_request_body import ResetRequestBody  # noqa: E501
from swagger_server.models.token_pair import TokenPair  # noqa: E501
from swagger_server.models.verifyemail_confirm_body import VerifyemailConfirmBody  # noqa: E501
from swagger_server.models.verifyemail_request_body import VerifyemailRequestBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_login_post(self):
        """Test case for auth_login_post

        Inicia sesión
        """
        body = LoginRequest()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_logout_post(self):
        """Test case for auth_logout_post

        Cierra sesión actual
        """
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/logout',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_password_reset_confirm_post(self):
        """Test case for auth_password_reset_confirm_post

        Confirma nuevo password
        """
        body = ResetConfirmBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/password/reset/confirm',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_password_reset_request_post(self):
        """Test case for auth_password_reset_request_post

        Solicita reset de contraseña
        """
        body = ResetRequestBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/password/reset/request',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_refresh_post(self):
        """Test case for auth_refresh_post

        Renueva access token con refresh token
        """
        body = AuthRefreshBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/refresh',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_register_post(self):
        """Test case for auth_register_post

        Alta de cuenta
        """
        body = RegisterRequest()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_verify_email_confirm_post(self):
        """Test case for auth_verify_email_confirm_post

        Confirma verificación de email
        """
        body = VerifyemailConfirmBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/verify-email/confirm',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_verify_email_request_post(self):
        """Test case for auth_verify_email_request_post

        Envía email de verificación
        """
        body = VerifyemailRequestBody()
        response = self.client.open(
            '/universidadpolitcnic-44f/Usuarios_y_autorizacion/1.0.0/auth/verify-email/request',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
