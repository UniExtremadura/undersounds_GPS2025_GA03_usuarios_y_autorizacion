import connexion
import six

from swagger_server.models.auth_refresh_body import AuthRefreshBody  # noqa: E501
from swagger_server.models.auth_response import AuthResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.register_request import RegisterRequest  # noqa: E501
from swagger_server.models.reset_confirm_body import ResetConfirmBody  # noqa: E501
from swagger_server.models.reset_request_body import ResetRequestBody  # noqa: E501
from swagger_server.models.token_pair import TokenPair  # noqa: E501
from swagger_server.models.verifyemail_confirm_body import VerifyemailConfirmBody  # noqa: E501
from swagger_server.models.verifyemail_request_body import VerifyemailRequestBody  # noqa: E501
from swagger_server import util


def auth_login_post(body):  # noqa: E501
    """Inicia sesión

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: AuthResponse
    """
    if connexion.request.is_json:
        body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_logout_post():  # noqa: E501
    """Cierra sesión actual

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def auth_password_reset_confirm_post(body):  # noqa: E501
    """Confirma nuevo password

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResetConfirmBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_password_reset_request_post(body):  # noqa: E501
    """Solicita reset de contraseña

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResetRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_refresh_post(body):  # noqa: E501
    """Renueva access token con refresh token

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: TokenPair
    """
    if connexion.request.is_json:
        body = AuthRefreshBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_register_post(body):  # noqa: E501
    """Alta de cuenta

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: AuthResponse
    """
    if connexion.request.is_json:
        body = RegisterRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_verify_email_confirm_post(body):  # noqa: E501
    """Confirma verificación de email

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VerifyemailConfirmBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_verify_email_request_post(body):  # noqa: E501
    """Envía email de verificación

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VerifyemailRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
