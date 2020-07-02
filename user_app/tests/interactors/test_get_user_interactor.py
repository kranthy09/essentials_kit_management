import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import NotFound
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface
from user_app.interactors.get_user \
    import GetUser


@pytest.mark.django_db
def test_get_user_interactor_with_invalid_username():

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
        interactor.get_user(user_ids=user_ids)

    # Assert

    storage.get_valid_user_ids \
        .assert_called_once_with(user_ids=user_ids)
    err = presenter.raise_exception_for_invalid_user_id \
        .call_args.kwargs['invalids']
    assert err['invalids'] == invalids