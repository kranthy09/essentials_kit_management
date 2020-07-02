import pytest
from common.oauth2_storage import OAuth2SQLStorage
from user_app.storages.storage_implementation \
    import StorageImplementation
from user_app.presenters.presenter_implementation \
    import PresenterImplementation
from user_app.interactors.oauth2_interactor \
    import OAuth2Interactor
from user_app.models.models import UserInfo


@pytest.mark.django_db
def test_for_oauth_interactor(user):

    # Arrange
    username = user.username
    password = user.password
    UserInfo.objects.create(username=username, password=password)

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()

    interactor = OAuth2Interactor(
                    storage=storage,
                    oauth2_storage=oauth2_storage
                )

    # Act
    response = interactor.login(
                    username=username,
                    password=password
                )

    # Assert