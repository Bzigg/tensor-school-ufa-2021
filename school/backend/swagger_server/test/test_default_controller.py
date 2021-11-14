# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response422 import InlineResponse422  # noqa: E501
from swagger_server.models.student_add_body import StudentAddBody  # noqa: E501
from swagger_server.models.student_auth_body import StudentAuthBody  # noqa: E501
from swagger_server.models.teatcher_auth_body import TeatcherAuthBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_api_student_add_post(self):
        """Test case for api_student_add_post

        запись на курс
        """
        body = StudentAddBody()
        response = self.client.open(
            '/Bzigg/tensor-school/1.0.0/api/student/add',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_student_auth_post(self):
        """Test case for api_student_auth_post

        Информация о студенте
        """
        body = StudentAuthBody()
        response = self.client.open(
            '/Bzigg/tensor-school/1.0.0/api/student/auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_teatcher_auth_post(self):
        """Test case for api_teatcher_auth_post

        Информация о преподавателе
        """
        body = TeatcherAuthBody()
        response = self.client.open(
            '/Bzigg/tensor-school/1.0.0/api/teatcher/auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
