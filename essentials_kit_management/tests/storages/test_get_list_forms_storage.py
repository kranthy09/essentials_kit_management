import pytest
from essentials_kit_management.storages \
    .storage_get_list_of_forms_implementation \
        import StorageListOfFormsImplementation
from essentials_kit_management.interactors \
    .storages.dtos import (FormDto,
                           UserItemDto,
                           UserBrandDto
                    )

@pytest.mark.django_db
def test_get_list_of_forms_dtos(user, form, section, item, brand, ordereditem):
    # Arrange
    user_id = 1
    offset = 0
    limit = 2
    form_dtos = [
        FormDto(
            form_id=1,
            form_name="Snacks Form",
            form_state="Live",
            delivery_date="2020-12-12",
            closing_date="2020-12-12"
        ),
        FormDto(
            form_id=2,
            form_name="Fruits Form",
            form_state="Done",
            delivery_date="2020-12-12",
            closing_date="2020-12-12"
        )
    ]

    storage = StorageListOfFormsImplementation()
    

    # Act
    result_form_dtos = storage.get_list_of_form_dtos(
                offset=offset,
                limit=limit
            )

    # Assert
    assert result_form_dtos == form_dtos

@pytest.mark.django_db
def test_get_user_item_dtos(user, form, section, item, brand, ordereditem):
    # Arrange
    user_id = 1
    form_ids = [1, 2]
    user_item_dtos = [
        UserItemDto(
            user_id=1,
            item_id=1,
            form_id=1
        ),
        UserItemDto(
            user_id=1,
            item_id=2,
            form_id=1
        ),
        UserItemDto(
            user_id=1,
            item_id=3,
            form_id=1
        ),
        UserItemDto(
            user_id=1,
            item_id=4,
            form_id=1
        )
    ]

    storage = StorageListOfFormsImplementation()

    # Act
    result_item_dtos = storage.get_user_item_dtos(
                            user_id=user_id,
                            form_ids=form_ids
                       )
    print(result_item_dtos)
    # Assert
    assert result_item_dtos == user_item_dtos

@pytest.mark.django_db
def test_get_user_brand_dtos(user, form, section, item, brand, ordereditem):
    # Arrange
    user_id = 1
    item_ids = [1, 2, 3, 4]
    user_brand_dtos = [
        UserBrandDto(
            brand_id=2,
            item_id=1,
            max_quantity=10,
            quantity=5,
            price_per_item=60,
            delivered_items=3,
            is_closed=False
        ),
        UserBrandDto(
            brand_id=4,
            item_id=2,
            max_quantity=10,
            quantity=8,
            price_per_item=60,
            delivered_items=5,
            is_closed=False
        ),
        UserBrandDto(
            brand_id=5,
            item_id=3,
            max_quantity=10,
            quantity=6,
            price_per_item=60,
            delivered_items=4,
            is_closed=False
        ),
        UserBrandDto(
            brand_id=8,
            item_id=4,
            max_quantity=10,
            quantity=7,
            price_per_item=60,
            delivered_items=3,
            is_closed=False
        )
    ]

    storage = StorageListOfFormsImplementation()

    # Act
    result_brand_dtos = storage.get_user_brand_dtos(
                            user_id=user_id,
                            item_ids=item_ids
                        )

    # Assert
    assert result_brand_dtos == user_brand_dtos
