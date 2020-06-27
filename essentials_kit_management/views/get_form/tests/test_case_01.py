"""
# TODO: Update test case description
"""
import json
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from essentials_kit_management.models.factories import FormFactory


REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"form_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetFormAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetFormAPITestCase, self).setupUser(
                username=username,
                password=password
            )
        FormFactory.create()

    def test_case(self):
        response = self.default_test_case()
        print(response.content)
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.