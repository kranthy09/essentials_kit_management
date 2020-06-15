import datetime
from abc import ABC, abstractmethod
from typing import List
from food_management.interactors.storages.dtos \
    import ItemQuantity


class StorageInterface:

    @abstractmethod
    def validate_meal_id(self, meal_id: int):
        pass

    @abstractmethod
    def validate_items_in_meal_id(self,
                                  meal_id: int,
                                  items: List[ItemQuantity]):
        pass

    @abstractmethod
    def validate_item_quantity_limit(self,
                                     items: List[ItemQuantity]
                                ):
        pass

    @abstractmethod
    def validate_order_date(self, date: datetime):
        pass

    @abstractmethod
    def validate_ordered_in_right_time(self,
                                       order_time: datetime,
                                       breakfast_time: datetime):
        pass

    @abstractmethod
    def validate_item_ids(self,
                          items: List[ItemQuantity]):
        pass

    @abstractmethod
    def vaildate_duplicate_item_ids(self,
                                    items: List[ItemQuantity]):
        pass