from user_app.common.dtos \
    import UserAuthTokensDTO
from user_app.interactors.storages.dtos \
    import UserDto
from user_app.exceptions.exceptions \
    import InvalidUsername, InvalidPassword
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import List


class PresenterImplementation(PresenterInterface):

    def raise_invalid_username(self):
        raise InvalidUsername

    def raise_invalid_username_and_password(self):
        raise InvalidPassword

    def raise_exception_for_invalid_user(self):
        pass

    def get_response_for_user_auth_token(self, user_auth_token_dto: UserAuthTokensDTO):
        response = {
            "user_id": user_auth_token_dto.user_id,
            "access_token": user_auth_token_dto.access_token,
            "refresh_token": user_auth_token_dto.refresh_token,
            "expires_in": str(user_auth_token_dto.expires_in)
        }
        return response

    def get_user_response(self, user_dtos: List[UserDto]):
        response = []
        for user_dto in user_dtos:
            response.append(
                    {
                        "user_id": user_dto.user_id,
                        "username": user_dto.username
                    }
                )
        return response