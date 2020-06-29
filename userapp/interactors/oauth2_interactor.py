from common.oauth2_storage import OAuth2SQLStorage
from essentials_kit_management.exceptions.exceptions\
    import InvalidUsername, InvalidPassword
from essentials_kit_management.interactors.presenters.presenter_interface\
    import PresenterInterface
from essentials_kit_management.interactors.storages \
    .storage_list_of_forms_interface \
        import StorageListOfFormsInterface
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService


class OAuth2Interactor:

    def __init__(self,
                 storage: StorageListOfFormsInterface,
                 oauth2_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface
                ):
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage
        self.storage = storage

    def login_wrapper(self,
              username: str,
              password: str):

        # validate username
        try:
            tokens_dto = self.login(username=username, password=password)
        except InvalidUsername:
            self.presenter.raise_invalid_username()
        except InvalidPassword:
            self.presenter.raise_invalid_username_and_password()

        response = self.presenter.get_response_for_user_auth_token(
                        user_tokens_dto=tokens_dto
                   )
        return response

    def login(self, username: str, password: str):

        self.storage.validate_username(username=username)
        user_id = self.storage.validate_username_and_password(
                            username=username,
                            password=password
                      )
        service = OAuthUserAuthTokensService(
                    oauth2_storage=self.oauth2_storage
                  )

        tokens_dto = service.create_user_auth_tokens(user_id)

        return tokens_dto
