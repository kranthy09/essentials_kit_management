# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_list_of_forms"
REQUEST_METHOD = "get"
URL_SUFFIX = "listofforms/"

from .test_case_01 import TestCase01GetListOfFormsAPITestCase

__all__ = [
    "TestCase01GetListOfFormsAPITestCase"
]
