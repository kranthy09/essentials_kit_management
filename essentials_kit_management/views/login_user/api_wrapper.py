import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from common.oauth2_storage import OAuth2SQLStorage



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    # ---------MOCK IMPLEMENTATION---------

    try:
        from essentials_kit_management.views.login_user.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from essentials_kit_management.views.login_user.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from essentials_kit_management.views.login_user.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="essentials_kit_management", test_case=test_case,
        operation_name="login_user",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]