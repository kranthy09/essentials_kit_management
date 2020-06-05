from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from essentials_kit_management.storages\
    .storage_implementation import StorageImplementation
from essentials_kit_management.presenters\
    .presenter_implementation import PresenterImplementation
from essentials_kit_management.interactors\
    .get_list_of_forms_interactor_v2\
        import GetListOfFormsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print(kwargs)
    user_id=kwargs['user_dto'].user_id
    print(f"userId:{user_id}")
    print("*"*20)
    kwargs['request_query_params']
    # offset = kwargs['offset']
    # limit = kwargs['limit']
    user_id = 4
    offset = 2
    limit = 5
    print("*"*20)
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetListOfFormsInteractor(
                    storage=storage,
                    presenter=presenter
                )
    response = interactor.get_list_of_forms(
                    user_id=user_id,
                    offset=offset,
                    limit=limit
                )
    return response

    
    # # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from essentials_kit_management.views.get_list_of_forms.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from essentials_kit_management.views.get_list_of_forms.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from essentials_kit_management.views.get_list_of_forms.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="essentials_kit_management", test_case=test_case,
    #     operation_name="get_list_of_forms",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]