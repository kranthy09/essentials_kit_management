"""
# TODO: Update test case description
"""
import json
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from essentials_kit_management.models.factories \
    import (FormFactory, UserFactory,
            SectionFactory, ItemFactory,
            BrandFactory, OrderedItemFactory)


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
        user = self.foo_user
        form = FormFactory(users=[user])
        section_1 = SectionFactory(form=form)
        section_2 = SectionFactory(form=form)
        item_1 = ItemFactory(section=section_1)
        item_2 = ItemFactory(section=section_2)
        brand_1 = BrandFactory(item=item_1)
        brand_2 = BrandFactory(item=item_1)
        brand_3 = BrandFactory(item=item_2)
        brand_4 = BrandFactory(item=item_2)
        order_1 = OrderedItemFactory(user=self.foo_user)
        order_2 = OrderedItemFactory(user=self.foo_user)
        order_3 = OrderedItemFactory(user=self.foo_user)

    def test_case(self):
        response = self.default_test_case()
        response_obj = json.loads(response.content)
        print(response_obj)
        # form = Form.objects.get(user_id=[])
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.