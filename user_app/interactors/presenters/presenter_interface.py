from abc import ABC, abstractmethod
from userapp.storages.dtos \
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
    def get_user_response(self, user_dtos: List[UserDto]):
        pass