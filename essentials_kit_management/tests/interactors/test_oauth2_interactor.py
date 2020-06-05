from unittest.mock import create_autospec,patch
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService
from essentials_kit_management.interactors.presenters.presenter_interface\
    import PresenterInterface
from essentials_kit_management.interactors.storages.storage_interface\
    import StorageInterface
from essentials_kit_management.interactors.oauth2_interactor\
    import OAuth2Interactor

@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
def test_oauth_interactor(create_user_auth_tokens):

    # Arrange
    user_id = 1
    username = 'monty'
    password = 'monty'
    tokens_dict = {
        "user_id": 1,
        "access_token": "mock_access_token",
        "refresh_token": "mock_refresh_token",
        "expires_in": 1000000000
    }
    tokens_dto = UserAuthTokensDTO(
            user_id=1,
            access_token="mock_access_token",
            refresh_token="mock_refresh_token",
            expires_in=1000000000
        )
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    interactor = OAuth2Interactor(
                    storage=storage,
                    presenter=presenter,
                    oauth2_storage=oauth2_storage
                 )

    storage.validate_username.return_value = "UsernameExits"
    storage.validate_username_and_password.return_value = user_id
    create_user_auth_tokens.return_value = tokens_dto
    presenter.get_response_for_user_auth_token.return_value = tokens_dict
    

    # Act
    response = interactor.login(
                        username=username,
                        password=password
                )

    # Assert
    assert response == tokens_dict
