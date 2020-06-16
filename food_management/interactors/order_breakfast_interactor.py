import datetime
from typing import List
from food_management.exceptions.exceptions \
    import (InvalidMealId,
            ItemNotFound,
            InvalidDate,
            InvalidItemId,
            InvalidOrderTime,
            InvalidDuplicateItem,
            InvalidItemQuantity)
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
                .raise_exception_for_item_not_found(items_not_in_meal=err)

        except InvalidItemQuantity as err:
            presenter \
                .raise_exception_for_item_quanity_limit_reached(
                        items=err
                    )
        except InvalidDate:
            presenter.raise_exception_for_invalid_order_date()

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
        # validate item ids
        self._check_item_ids_are_valid(items=order.items)
        # items in meal validation
        self._check_items_in_meal(meal_id = order.meal_id,
                                  items=order.items)
        # order quantity validation
        self._check_item_invalid_quantity(request_items=order.items)
        # order date validation
        self._check_order_date(meal_id=order.meal_id,
                               order_date=order.date,
                               order_time=order.order_time)
        # validate duplicate item ids
        self.storage.vaildate_duplicate_item_ids(items=order.items)

    def _check_item_ids_are_valid(self, items: List[ItemQuantity]):
        item_ids = [item.item_id for item in items]
        all_items_in_storage \
            = self.storage.validate_item_ids(item_ids=item_ids)
        invalid_item_ids = []
        for item_id in item_ids:
            is_item_id_not_in_storage = not(item_id in all_items_in_storage)
            if is_item_id_not_in_storage:
                invalid_item_ids.append(item_id)
        if invalid_item_ids:
            raise InvalidItemId(item_ids=invalid_item_ids)
        

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

    def _check_item_invalid_quantity(self, request_items: List[ItemQuantity]):

        items_with_invalid_quantity = []
        for item in request_items:
            is_invalid_quantity = item.quantity < 0
            if is_invalid_quantity:
                items_with_invalid_quantity.append(
                        item.item_id
                    )
        if items_with_invalid_quantity:
            raise InvalidItemQuantity(items=items_with_invalid_quantity)

    def _check_order_date(self,
                          meal_id: int,
                          order_date: datetime,
                          order_time: datetime):
        meal_valid_date = self.storage.validate_order_date(meal_id=meal_id)
        is_not_order_date_valid = not(meal_valid_date.date() >= order_date.date())
        is_order_date_valid = meal_valid_date.date() == order_date.date()
        if is_not_order_date_valid:
            raise InvalidDate
        elif is_order_date_valid:
            meal_valid_time = self.storage.validate_ordered_in_right_time(meal_id=meal_id)
            is_not_order_in_right_time = not(order_time.time() < meal_valid_time.time())
            if is_not_order_in_right_time:
                raise InvalidOrderTime