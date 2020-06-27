import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from essentials_kit_management.storages.storage_implementation \
    import StorageImplementation
from essentials_kit_management.presenters.presenter_implementation \
    import PresenterImplementation
from essentials_kit_management.interactors.get_form \
    import GetForm
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs['user'].id
    form_id = kwargs['form_id']

    storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetForm(
                    storage=storage
                )
    response = interactor.get_form_sections_wrapper(
                    user_id=user_id,
                    form_id=form_id,
                    presenter=presenter
                )
    response_data = json.dumps(response)
    print(response_data)
    return HttpResponse(response_data, status=200)