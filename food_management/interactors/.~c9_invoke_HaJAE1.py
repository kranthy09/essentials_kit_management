from typing import List
from food_management.exceptions.exceptions \
    import (InvalidMealId,
            ItemNotFound,
            InvalidDate,
            InvalidItemId,
            InvalidOrderTime,
            InvalidDuplicateItem,
            ItemQuantiyLimitReached)
from food_management.interactors.storages.dtos \
    import (OrderDto,
            ItemQuantity)
from food_management.interactors.storages \
    .storage_interface import StorageInterface
from food_management.interactors.presenters \
    .presenter_interface import PresenterInterface


class OrderBreakFastInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    # TODO : validate meal_id
    # TODO : validate that meal contains given item_ids - 
    # TODO : validate that item has given required quantity
    # TODO : validate item ids are in database 
    # TODO : validate duplicate items - 
    # TODO : validate, ordered in right time before two hours - 
    # TODO : validate, ordered date - 
    # TODO : to be continued
    
    def order_breakfast_wrapper(
                        self,
                        order: OrderDto,
                        presenter: PresenterInterface
                ):
        try:
            self.order_breakfast(
                    order=order
            )
        except InvalidMealId:
            presenter.raise_exception_for_invalid_meal_id()

        except InvalidItemId as err:
            presenter.raise_exception_for_invalid_item_ids(item_ids=err)

        except ItemNotFound as err:
            presenter \

        except ItemQuantiyLimitReached:
            presenter.raise_exception_for_item_quanity_limit_reached()

        except InvalidDate:
            presenter.raise_exception_for_order_invalid_date()

        except InvalidOrderTime:
            presenter.raise_exception_for_invalid_order_time()

        except InvalidDuplicateItem as err:
            presenter.raise_exception_for_invalid_duplicate_items_ids(err)


    def order_breakfast(
                    self,
                    order: OrderDto
                ):

        # meal_id validation
        self.storage.validate_meal_id(order.meal_id)
        # items in meal validation
        self._check_items_in_meal(meal_id = order.meal_id,
                                  items=order.items)
        # order limit validation
        self.storage.validate_item_quantity_limit(order.items)
        # order date validation
        self.storage.validate_order_date(order.date)
        # order time(has to check after the date is checked)
        self.storage \
            .validate_ordered_in_right_time(
                                order_time=order.order_time,
                                breakfast_time = order.order_deadline_time
                            )
        # validate item ids
        self.storage.validate_item_ids(items=order.items)
        # validate duplicate item ids
        self.storage.vaildate_duplicate_item_ids(items=order.items)


    def _check_items_in_meal(self,
                             meal_id: int,
                             items: List[ItemQuantity]
                        )-> List[int]:
        meal_items = self.storage \
            .validate_items_in_meal_id(items=items,
                                       meal_id=meal_id)
        item_ids = [item.item_id for item in items]
        items_not_in_meal \
            = [item_id for item_id in item_ids \
                if item_id not in meal_items]

        if items_not_in_meal:
            raise ItemNotFound(
                    items_not_in_meal=items_not_in_meal)