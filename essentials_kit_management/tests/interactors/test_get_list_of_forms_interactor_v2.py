import pytest
from unittest.mock import create_autospec
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface


@pytest.mark.django_db
def test_get_list_of_forms_interactor():

    # Arrange
    user_id = 1
    offset = 0
    limit = 5

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    

    # Act


    # Assert