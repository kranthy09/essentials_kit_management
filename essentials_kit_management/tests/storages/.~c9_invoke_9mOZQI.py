import pytest
from essentials_kit_management.storages \
    .storage_implementation \
        import StorageImplementation
from essentials_kit_management.interactors \
    .storages.dtos


def test_get_list_of_forms_dtos(users, forms, sections, items, brands):
    # Arrange
    user_id = 1
    offset = 0
    limit = 2
    form_dtos = [
        FormDto(
            form_id=1,
            form_name="Snacks Form",
            form_state="LIVE",
            delivery_date="2020-12-12",
            closing_date="2020-12-12"
        )
    ]

    storage = StorageImplementation()
    

    # Act
    result_form_dtos = storage.get_list_of_form_dtos(
                user_id=user_id,
                offset=offset,
                limit=limit
            )

    # Assert
    assert result_form_dtos == form_dtos