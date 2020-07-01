from user_app.common.dtos \
    import UserAuthTokensDTO
from user_app.interactors.storages.dtos \
    import UserDto
from common.oauth2_storage import OAuth2SQLStorage
from user_app.interactors.oauth2_interactor \
    import OAuth2Interactor
from user_app.storages.storage_implementation \
    import StorageImplementation
from user_app.interactors.get_user \
    import GetUser
from typing import List


class ServiceInterface:

    @staticmethod
    def get_tokens_dto(username: str, password: str)-> \
        UserAuthTokensDTO:
        storage = StorageImplementation()
        oauth2_storage = OAuth2SQLStorage()
        interactor = OAuth2Interactor(
                        storage=storage,
                        oauth2_storage=oauth2_storage
                    )
        tokens_dto = interactor.login(
                            username=username,
                            password=password)
        return tokens_dto

    @staticmethod
    def get_user_details(user_ids: List[int])-> \
        List[UserDto]:
        storage = StorageImplementation()
        interactor = GetUser(storage=storage)
        user_dtos = interactor.get_user(user_ids=user_ids)
        return user_dtos