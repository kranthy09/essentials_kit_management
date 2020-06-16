from abc import ABC
from abc import abstractmethod
from typing import List


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def raise_invalid_post_id_exception(self):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_meal_id(self):
        pass

    @abstractmethod
    def raise_exception_for_item_not_found(
                                    self,
                                    items_not_in_meal: List[int]
                                ):
        pass

    @abstractmethod
    def raise_exception_for_item_quanity_limit_reached(
                        self,
                        items: List[int]
                    ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_order_date(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_order_time(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_ids(self,
                                    item_ids: List[int]
                                    ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_duplicate_items_ids(
                                        self,
                                        item_ids: List[int]
                            ):
        pass