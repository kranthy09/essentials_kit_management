from userapp.exceptions.exceptions \
    import InvalidUserId
from userapp.interactors.storages.storage_interface \
    import StorageInterface
from userapp.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import List


class GetUser:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):

        self.presenter = presenter
        self.storage = storage

    def get_user_wrapper(self, user_ids: int, presenter: PresenterInterface):

        try:
            user_dtos = self.get_user(user_ids=user_ids)
        except InvalidUserId as err:
            presenter.raise_exception_for_invalid_user(invalids=err)

        response = presenter.get_user_response(user_dtos)
        return response
    def get_user(self, user_ids: int):

        self._validate_user_ids(user_ids=user_ids)
        user_dtos = self.storage.get_user_details(user_ids=user_ids)
        return user_dtos

    def _validate_user_ids(self, user_ids: List[int]):

        valids = self.storage.get_valid_user_ids(user_ids=user_ids)
        invalids = [user_id for user_id in user_ids
                    if user_id not in valids]
        if invalids:
            raise InvalidUserId(invalids=invalids)