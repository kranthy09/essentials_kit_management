import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import NotFound
from user_app.interactors.storages.dtos \
    import UserDto
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface
from user_app.interactors.get_user \
    import GetUser


@pytest.mark.django_db
def test_get_user_interactor_with_invalid_user_id():

    # Arrange
    user_ids = [1, 2, 4, 100, 200]
    valids = [1, 2, 4]
    invalids = [100, 200]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetUser(storage=storage)

    storage.get_valid_user_ids.return_value = valids
    presenter.raise_exception_for_invalid_user_id \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_user_wrapper(
            user_ids=user_ids,
            presenter=presenter
        )

    # Assert

    storage.get_valid_user_ids \
        .assert_called_once_with(user_ids=user_ids)
    err = presenter.raise_exception_for_invalid_user_id \
        .call_args.kwargs['invalids']
    assert err.invalids == invalids

@pytest.mark.django_db
def test_get_user_interactor():

    # Arrange
    user_ids = [1, 2]
    valids = [1, 2]
    user_dtos = [
        UserDto(
            user_id=1,
            username="bellamy"
        ),
        UserDto(
            user_id=2,
            username="maya"
        )
    ]

    user_response = [
        {
            "user_id": 1,
            "username": "bellamy"
        },
        {
            "user_id": 2,
            "username": "maya"
        }
    ]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetUser(storage=storage)

    storage.get_valid_user_ids.return_value = valids
    storage.get_user_details.return_value = user_dtos
    presenter.get_user_response.return_value = user_response

    # Act
    response = interactor.get_user_wrapper(
                        user_ids=user_ids,
                        presenter=presenter
                    )

    # Assert

    storage.get_valid_user_ids \
        .assert_called_once_with(user_ids=user_ids)
    presenter.get_user_response \
        .assert_called_once_with(user_dtos=user_dtos)
    assert response == user_response

