import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import BadRequest, NotFound
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from essentials_kit_management.interactors \
    .get_section_items import GetSectionItems
from essentials_kit_management.interactors \
    .get_item_brands import GetBrands


def test_get_section_items_for_duplicate_section_ids():

    # Arrange
    section_ids = [1, 2, 3, 3, 2]
    duplicates = [2, 3]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetSectionItems(storage=storage)

    presenter.raise_exception_for_duplicate_section_ids \
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_section_items_wrapper(
                        section_ids=section_ids,
                        presenter=presenter
                    )

    # Assert
    err = presenter.raise_exception_for_duplicate_section_ids \
        .call_args.kwargs['duplicates']
    assert err.duplicates == duplicates

def test_get_section_items_for_invalid_section_ids():

    # Arrange
    section_ids = [1, 2, 3, 400, 500]
    valid_section_ids = [1, 2, 3]
    invalid_section_ids = [400, 500]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetSectionItems(storage=storage)

    storage.get_valid_section_ids \
        .return_value = valid_section_ids
    presenter.raise_exception_for_invalid_section_ids \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_section_items_wrapper(
                        section_ids=section_ids,
                        presenter=presenter
                    )

    # Assert
    storage.get_valid_section_ids \
        .assert_called_once_with(section_ids=section_ids)
    err = presenter.raise_exception_for_invalid_section_ids \
        .call_args.kwargs['invalids']
    assert err.invalids == invalid_section_ids

@patch.object(GetBrands, 'get_brands')
def test_get_section_items(get_brands_mock,
                           section_items_dtos,
                           item_details_dtos,
                           get_sections_mock_response,
                           items_details_with_brands_dto,
                           sections_complete_details_dto):

    section_ids = [1, 2]
    valid_section_ids = [1, 2]
    item_ids = [item_details_dto.item_id 
                for item_details_dto in item_details_dtos]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetSectionItems(storage=storage)

    storage.get_valid_section_ids \
        .return_value = valid_section_ids
    storage.get_section_item_dtos \
        .return_value = section_items_dtos
    storage.get_item_details \
        .return_value = item_details_dtos
    get_brands_mock.return_value = items_details_with_brands_dto
    presenter.get_section_items_response\
        .return_value = get_sections_mock_response

    # Act
    response = interactor.get_section_items_wrapper(
                    section_ids=section_ids,
                    presenter=presenter
                )

    # Assert
    storage.get_valid_section_ids \
        .assert_called_once_with(section_ids=section_ids)
    storage.get_section_item_dtos \
        .assert_called_once_with(section_ids=section_ids)
    storage.get_item_details \
        .assert_called_once_with(item_ids=item_ids)
    presenter.get_section_items_response \
        .assert_called_once_with(
            sections_complete_details_dto \
                =sections_complete_details_dto)
    assert response == get_sections_mock_response
