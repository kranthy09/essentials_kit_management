import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from essentials_kit_management.storages.storage_implementation\
    import StorageImplementation
from essentials_kit_management.presenters.presenter_implementation\
    import PresenterImplementation
from essentials_kit_management.adapters.service_adapter \
    import get_service_adapter
from common.oauth2_storage import OAuth2SQLStorage



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    username = kwargs['username']
    password = kwargs['password']
    presenter = PresenterImplementation()
    service_adapter = get_service_adapter()
    tokens_dto = service_adapter \
                    .auth_service.get_user_tokens_dto(
                                username=username, password=password)
    response = presenter \
        .get_response_for_user_auth_token(
                    user_tokens_dto=tokens_dto)

    response_data = json.dumps(response)

    return HttpResponse(response_data, status=201)
