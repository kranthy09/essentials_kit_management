from essentials_kit_management.dtos.dtos \
    import OrderListDto
from essentials_kit_management.interactors.storages \
    .storage_interface import StorageInterface
from essentials_kit_management.interactors.presenters \
    .presenter_interface import PresenterInterface
from typing import List, Dict


class PostFormInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def post_form(self, order_list_dto: OrderListDto
            )-> List[Dict[str, str]]:

        section_d
