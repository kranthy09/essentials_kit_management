from abc import ABC, abstractmethod
from user_app.common.dtos \
    import UserAuthTokensDTO
from user_app.interactors.storages.dtos \
    import UserDto
from typing import List


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username(self):
        pass

    @abstractmethod
    def raise_invalid_username_and_password(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def get_response_for_user_auth_token(self, user_auth_token_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def get_user_response(self, user_dtos: List[UserDto]):
        pass