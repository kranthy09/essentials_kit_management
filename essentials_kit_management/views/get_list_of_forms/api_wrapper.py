import json
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from essentials_kit_management.storages \
    .storage_implementation \
        import StorageImplementation 
from essentials_kit_management.presenters \
    .presenter_implementation import PresenterImplementation
from essentials_kit_management.interactors \
    .get_list_of_forms_interactor \
        import GetListOfFormsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_dto'].user_id
    query_params = kwargs['request_query_params']
    limit = query_params.limit
    offset = query_params.offset
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetListOfFormsInteractor(
                    storage=storage,
                    presenter=presenter
                )
    result = interactor.get_list_of_forms(
                    user_id=user_id,
                    offset=offset,
                    limit=limit
                )
    response = json.dumps(result)
    return response
