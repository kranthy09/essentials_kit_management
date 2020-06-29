from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_username_and_password(self, username: str, password: str):
        pass

    @abstractmethod
    def get_valid_user_ids(self, user_ids: int):
        pass

    @abstractmethod
    def get_user_details(self, user_ids: int):
        pass