# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_form"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/{form_id}/"

from .test_case_01 import TestCase01GetFormAPITestCase

__all__ = [
    "TestCase01GetFormAPITestCase"
]
