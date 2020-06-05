# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "login_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "signin/"

from .test_case_01 import TestCase01LoginUserAPITestCase

__all__ = [
    "TestCase01LoginUserAPITestCase"
]
