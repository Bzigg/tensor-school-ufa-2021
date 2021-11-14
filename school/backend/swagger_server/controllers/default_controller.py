import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response422 import InlineResponse422  # noqa: E501
from swagger_server.models.student_add_body import StudentAddBody  # noqa: E501
from swagger_server.models.student_auth_body import StudentAuthBody  # noqa: E501
from swagger_server.models.teatcher_auth_body import TeatcherAuthBody  # noqa: E501
from swagger_server import util


def api_student_add_post(body=None):  # noqa: E501
    """запись на курс

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = StudentAddBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_student_auth_post(body=None):  # noqa: E501
    """Информация о студенте

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = StudentAuthBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_teatcher_auth_post(body=None):  # noqa: E501
    """Информация о преподавателе

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = TeatcherAuthBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
