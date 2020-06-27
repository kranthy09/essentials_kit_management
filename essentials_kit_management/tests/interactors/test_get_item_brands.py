import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import BadRequest, NotFound
from essentials_kit_management.exceptions.exceptions \
    import UniqueItemException
from essentials_kit_management.interactors.get_brands \
    import GetBrands
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface


def test_get_brands_for_duplicate_item_ids():

    # Arrange
    item_ids = [1, 2, 3, 3, 2]
    duplicates = [2, 3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetBrands(storage=storage)

    presenter.raise_exception_for_unique_item_expected \
        .side_effect = BadRequest
    # Act
    with pytest.raises(BadRequest):
        interactor.get_brands_wrapper(
                    item_ids=item_ids,
                    presenter=presenter
                )

    # Assert
    err = presenter.raise_exception_for_unique_item_expected \
        .call_args.kwargs['duplicates']
    assert err.duplicates == duplicates

def test_get_brands_for_invalid_item_ids():

    # Arrange
    item_ids = [1, 2, 3, 100, 200]
    valid_item_ids = [1, 2, 3]
    invalid_item_ids = [100, 200]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetBrands(storage=storage)

    storage.get_valid_item_ids \
        .return_value = valid_item_ids
    presenter.raise_exception_for_invalid_item_ids \
        .side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.get_brands_wrapper(
                    item_ids=item_ids,
                    presenter=presenter
                )

    # Assert
    err = presenter.raise_exception_for_invalid_item_ids \
        .call_args.kwargs['invalids']
    assert err.invalids == invalid_item_ids

def test_get_posts(item_brands_dtos, brand_details_dtos, 
                    get_brands_mock_response,
                    items_details_with_brands_dto):

    # Arrange
    item_ids = [1, 2]
    valid_item_ids = [1, 2]
    brand_ids = [item_brand_dto.brand_id
                for item_brand_dto in item_brands_dtos]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetBrands(storage=storage)

    storage.get_valid_item_ids \
        .return_value = valid_item_ids
    storage.get_item_brands \
        .return_value = item_brands_dtos
    storage.get_brand_details \
        .return_value = brand_details_dtos
    presenter.get_brands_response \
        .return_value = get_brands_mock_response

    # Act
    response = interactor.get_brands_wrapper(
                    item_ids=item_ids,
                    presenter=presenter
                )

    # Assert
    storage.get_valid_item_ids \
        .assert_called_once_with(item_ids=item_ids)
    storage.get_brand_details \
        .assert_called_once_with(brand_ids=brand_ids)
    presenter.get_brands_response \
        .assert_called_once_with(
            items_with_brands=items_details_with_brands_dto)
    assert response == get_brands_mock_response