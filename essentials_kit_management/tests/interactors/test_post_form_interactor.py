from unittest.mock import create_autospec
from essentials_kit_management.dtos.dtos \
    import (PostItemDto,
            OrderListDto,
            PostSectionDto
        )
from essentials_kit_management.interactors.storages\
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters\
    .presenter_interface import PresenterInterface
from essentials_kit_management.interactors \
    .post_form_interactor import PostFormInteractor


def test_post_form_interactor_update_order():
    # Arrange
    user_id = 1,
    is_order_exists = True
    mock_response = "Success"
    post_item_dtos = [
            PostItemDto(
                item_id=1,
                brand_id=1,
                selected_quantity=6,
            ),
            PostItemDto(
                item_id=2,
                brand_id=2,
                selected_quantity=6,
            )
        ]
    post_section_dtos = [
            PostSectionDto(
                section_id=1,
                item_id=1
            ),
            PostSectionDto(
                section_id=2,
                item_id=2
            )
        ]
    order_list_dto = OrderListDto(
                section_item_dtos=post_section_dtos,
                item_brand_dtos=post_item_dtos
        )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = PostFormInteractor(
                    storage=storage,
                    presenter=presenter
                 )
    storage.get_order.return_value = is_order_exists
    presenter.get_response_for_post_form.return_value = mock_response

    # Act
    response = interactor.post_form(
                        user_id=user_id,
                        order_list_dto=order_list_dto
                    )

    # Assert
    storage.get_order.assert_called()
    storage.update_order.assert_called()
    presenter.get_response_for_post_form.assert_called()
    assert response == mock_response