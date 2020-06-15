from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface


class InvalidUserId(Exception):
    pass

class InvalidLimit(Exception):
    pass

class InvalidOffSet(Exception):
    pass

class GetListofFormsInteractor:

    def __init__(self,
                 storage: StorageInterface
                ):
        self.storage = storage

    def list_of_forms_wrapper(
                        self,
                        user_id: int,
                        offset: int,
                        limit: int,
                        presenter: PresenterInterface
                    ):

        try:
            self.get_list_of_forms(
                    user_id=user_id,
                    offset=offset,
                    limit=limit
                )
        except InvalidUserId:
            presenter.raise_expection_for_invalid_user_id(user_id)
        except InvalidOffSet:
            presenter.raise_invalid_offset(offset)
        except InvalidLimit:
            presenter.raise_invalid_limit(limit)

    def get_list_of_forms(
                    self,
                    user_id: int,
                    offset: int,
                    limit: int
                ):
        self.storage.is_valid_user_id(user_id=user_id)
        self._is_valid_offset(offset=offset)
        self._is_valid_limit(limit=limit)

    
    def _is_valid_offset(self, offset: int):

        if offset < 0:
            raise InvalidOffSet

    def _is_valid_limit(self, limit: int):

        if limit < 0:
            raise InvalidLimit