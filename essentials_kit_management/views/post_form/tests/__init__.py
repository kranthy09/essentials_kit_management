# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "post_form"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/form/"

from .test_case_01 import TestCase01PostFormAPITestCase

__all__ = [
    "TestCase01PostFormAPITestCase"
]
