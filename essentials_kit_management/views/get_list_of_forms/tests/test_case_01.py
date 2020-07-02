"""
# TODO: Update test case description
"""
import json
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from essentials_kit_management.models.models \
    import Form, FormUser
from essentials_kit_management.models.factories \
    import (FormFactory,
            SectionFactory, ItemFactory,
            BrandFactory, OrderedItemFactory)

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"offset": 0, "limit": 3},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetListOfFormsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetListOfFormsAPITestCase, self).setupUser(
                username=username, password=password
            )
        user = self.foo_user
        print("\n"*10)
        print(user.id)
        form = FormFactory()
        section_1 = SectionFactory(form=form)
        section_2 = SectionFactory(form=form)
        item_1 = ItemFactory(section=section_1)
        item_2 = ItemFactory(section=section_2)
        brand_1 = BrandFactory(item=item_1)
        brand_2 = BrandFactory(item=item_1)
        brand_3 = BrandFactory(item=item_2)
        brand_4 = BrandFactory(item=item_2)
        order_1 = OrderedItemFactory(user_id=self.foo_user.id)
        order_2 = OrderedItemFactory(user_id=self.foo_user.id)
        order_3 = OrderedItemFactory(user_id=self.foo_user.id)

    def test_case(self):

        print("\n"*10)
        forms = FormUser.objects.filter(user_id=self.foo_user.id).select_related('form')
        print(forms)
        response = self.default_test_case()
        response_obj = json.loads(response.content)
        form = response_obj[0]
        form_obj = Form.objects.get(id=form['form_id'])
        
        self.assert_match_snapshot(
                name="form_id",
                value = form_obj.id
            )
        self.assert_match_snapshot(
                name="form_name",
                value=form_obj.title
            )
        self.assert_match_snapshot(
                name="form_state",
                value=form_obj.state
            )
        self.assert_match_snapshot(
                name="closing_date",
                value=form_obj.closed_date
            )
        self.assert_match_snapshot(
                name="next_delivery_date",
                value=form_obj.expected_delivery_date
            )
        self.assert_match_snapshot(
                name="total_items",
                value=21
            )
        self.assert_match_snapshot(
                name="total_cost_estimate",
                value=1535
            )
        self.assert_match_snapshot(
                name="pending_items",
                value=2
            )
        self.assert_match_snapshot(
                name="cost_incurred",
                value=1696
            )
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.