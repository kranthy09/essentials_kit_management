from essentials_kit_management.dtos.dtos \
    import OrderListDto
from essentials_kit_management.exceptions\
    .exceptions import OrderedItemDoesNotExist
from essentials_kit_management.interactors.storages.storage_interface \
    import StorageInterface
from essentials_kit_management.interactors.presenters\
    .presenter_interface import PresenterInterface
from typing import List, Dict


class PostFormInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def post_form(self, user_id: int,
                  order_list_dto: OrderListDto
                )-> List[Dict[str, str]]:
        item_brand_dtos = order_list_dto.item_brand_dtos
        for item_brand_dto in item_brand_dtos:
            is_order_exists = self.storage.get_order(
                                user_id=user_id,
                                item_id=item_brand_dto.item_id,
                                brand_id=item_brand_dto.brand_id
                            )
            if is_order_exists:
                self.storage.update_order(user_id, item_brand_dto)
            else:
                self.storage.create_order(user_id, item_brand_dto)
        response = self.presenter.get_response_for_post_form()
        return response