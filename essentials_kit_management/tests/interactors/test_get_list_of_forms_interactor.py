from unittest.mock import create_autospec
from essentials_kit_management.constants.enums\
    import FormStateType
from essentials_kit_management.interactors.storages \
    .dtos import (FormDto,
                  UserItemDto,
                  UserBrandDto
                )
from essentials_kit_management.interactors\
    .storages.storage_list_of_forms_interface\
        import StorageListOfFormsInterface
from essentials_kit_management.interactors\
    .presenters.presenter_interface\
        import PresenterInterface
from essentials_kit_management.interactors\
    .get_list_of_forms_interactor\
        import GetListOfFormsInteractor


def test_get_list_of_forms_interactor():
    # Arrange
    user_id = 1
    offset = 0
    limit = 2
    form_ids = [1,2]
    form_dtos = [
        FormDto(
            form_id=1,
            form_name="Snacks Form",
            form_state=FormStateType.LIVE.value,
            delivery_date="2020-06-09",
            closing_date="2020-06-12"
        ),
        FormDto(
            form_id=2,
            form_name="Fruits Form",
            form_state=FormStateType.DONE.value,
            delivery_date="2020-06-09",
            closing_date="2020-06-12"
        )
        ]
    user_item_dtos = [
            UserItemDto(
                form_id=1,
                item_id=1,
                user_id=1
            ),
            UserItemDto(
                form_id=2,
                item_id=2,
                user_id=1
            )
        ]
    user_brand_dtos = [
            UserBrandDto(
                brand_id=1,
                item_id=1,
                max_quantity=0,
                quantity=0,
                price_per_item=0,
                delivered_items=0,
                is_closed=False
            ),
            UserBrandDto(
                brand_id=1,
                item_id=2,
                max_quantity=20,
                quantity=10,
                price_per_item=30,
                delivered_items=6,
                is_closed=False
            )
        ]
    mock_response = [
        {
            'form_id': 1,
            'form_name': 'Snacks Form',
            'form_state': FormStateType.LIVE.value,
            'delivery_date': '2020-06-09',
            'closing_date': '2020-06-12',
            'total_items': 0,
            'total_cost_estimate': 0,
            'pending_items': 0,
            'cost_incurred': 0
        },
        {
            'form_id': 2,
            'form_name': 'Fruits Form',
            'form_state': FormStateType.CLOSED.value,
            'delivery_date': '2020-06-09',
            'closing_date': '2020-06-12',
            'total_items': 10,
            'total_cost_estimate': 300,
            'pending_items': 4,
            'cost_incurred': 120
        }
    ]

    storage = create_autospec(StorageListOfFormsInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetListOfFormsInteractor(
                    storage=storage,
                    presenter=presenter
                 )

    storage.get_list_of_form_dtos.return_value = form_dtos
    storage.get_user_item_dtos.return_value = user_item_dtos
    storage.get_user_brand_dtos.return_value = user_brand_dtos
    presenter.get_response_for_list_of_forms.return_value = mock_response
    # Act
    response = interactor.get_list_of_forms(
                    user_id=user_id,
                    offset=offset,
                    limit=limit
                )

    # Assert
    storage.get_list_of_form_dtos.assert_called_once()
    storage.get_user_item_dtos.assert_called_once()
    storage.get_user_brand_dtos.assert_called_once()
    presenter.get_response_for_list_of_forms.assert_called_once()
    assert response == mock_response