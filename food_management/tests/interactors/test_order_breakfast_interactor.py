import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import (NotFound,
            InvalidRequestTypeException)
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
from food_management.interactors.order_breakfast_interactor \
    import OrderBreakFastInteractor


def test_order_item_interactor_validate_meal_id():

    # Arrange
    meal_id = 100
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4,
        ),
        ItemQuantity(
            item_id=2,
            quantity=3,
        )
    ]
    date = "2020-10-4"
    order_time="6:34:21"
    order_deadline_time = "7:00:00"
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                order_deadline_time=order_deadline_time,
                order_time=order_time,
                items=items
            )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                    storage=storage
                 )
    storage.validate_meal_id.side_effect = InvalidMealId
    presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor \
            .order_breakfast_wrapper(presenter=presenter,
                                     order=order)

    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_meal_id.assert_called_once()

def test_order_item_interactor_validate_items_in_meal():

    # Arrange
    meal_id = 50
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4
        ),
        ItemQuantity(
            item_id=2,
            quantity=6
        ),
        ItemQuantity(
            item_id=4,
            quantity=3
        )
    ]
    date = "2020-04-19"
    order_time = "10:12:19"
    order_deadline_time = "7:00:00"
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                    storage=storage
                 )
    storage.validate_items_in_meal_id.side_effect = ItemNotFound
    presenter.raise_exception_for_item_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.order_breakfast_wrapper(
                order=order,
                presenter=presenter
            )
    storage \
        .validate_items_in_meal_id \
            .assert_called_once_with(meal_id=meal_id,
                                     items=items)
    presenter.raise_exception_for_item_not_found.assert_called_once()

def test_order_item_interactor_item_quantity_limit():

    # Arrange
    meal_id = 4
    items = [
        ItemQuantity(
            item_id=1,
            quantity=5
        ),
        ItemQuantity(
            item_id=4,
            quantity=6
        )
    ]
    date = "2020-4-9"
    order_time="9:34:21"
    order_deadline_time = "7:00:00"
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                    storage=storage
                 )

    storage.validate_item_quantity_limit \
        .side_effect = ItemQuantiyLimitReached
    presenter.raise_exception_for_item_quanity_limit_reached \
        .side_effect = InvalidRequestTypeException

    # Act    
    with pytest.raises(InvalidRequestTypeException):
        interactor \
            .order_breakfast_wrapper(order=order,
                                     presenter=presenter)

    storage.validate_item_quantity_limit.assert_called_once_with(items)
    presenter.raise_exception_for_item_quanity_limit_reached.assert_called_once()

def test_order_item_interactor_order_invalid_date():

    # Arrange
    meal_id = 5
    date = "2020-9-5"
    order_time = "10:12:48"
    order_deadline_time = "7:00:00"
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4
        ),
        ItemQuantity(
            item_id=2,
            quantity=5
        )
    ]
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                        storage=storage
                 )

    storage.validate_order_date \
        .side_effect = InvalidDate
    presenter.raise_exception_for_order_invalid_date \
        .side_effect = InvalidRequestTypeException

    with pytest.raises(InvalidRequestTypeException):
        interactor.order_breakfast_wrapper(
                        order=order,
                        presenter=presenter
                   )
    storage.validate_order_date \
        .assert_called_once_with(date=date)
    presenter.raise_exception_for_order_invalid_date \
        .assert_called_once()

def test_order_item_interactor_with_order_in_right_time():

    # Arrange
    meal_id = 5
    date = "2020-9-5"
    order_time = "10:34:11"
    order_deadline_time = "7:00:00"
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4
        ),
        ItemQuantity(
            item_id=2,
            quantity=5
        )
    ]
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                        storage=storage
                 )

    storage.validate_ordered_in_right_time \
        .side_effect = InvalidOrderTime
    presenter.raise_exception_for_invalid_order_time \
        .side_effect = InvalidRequestTypeException

    with pytest.raises(InvalidRequestTypeException):
        interactor.order_breakfast_wrapper(
                        order=order,
                        presenter=presenter
                   )

    storage.validate_ordered_in_right_time \
        .assert_called_once_with(
            order_time=order_time,
            breakfast_time=order_deadline_time
        )
    presenter.raise_exception_for_invalid_order_time \
        .assert_called_once()

def test_order_item_interactor_with_invalid_item_ids():

    # Arrange
    meal_id = 5
    date = "2020-9-5"
    order_time = "10:34:11"
    order_deadline_time = "7:00:00"
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4
        ),
        ItemQuantity(
            item_id=2,
            quantity=5
        )
    ]
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )
    item_ids = [1]
    err  = InvalidItemId(item_ids)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                        storage=storage
                 )

    storage.validate_item_ids \
        .side_effect = err
    presenter.raise_exception_for_invalid_item_ids \
        .side_effect = InvalidRequestTypeException

    with pytest.raises(InvalidRequestTypeException):
        interactor \
            .order_breakfast_wrapper(order=order,
                                     presenter=presenter)

    storage.validate_item_ids \
        .assert_called_once_with(items=items)
    presenter.raise_exception_for_invalid_item_ids \
        .assert_called_once()

def test_order_item_interactor_with_invalid_duplicate_item_ids():

    # Arrange
    meal_id = 5
    date = "2020-9-5"
    order_time = "10:34:11"
    order_deadline_time = "7:00:00"
    items = [
        ItemQuantity(
            item_id=1,
            quantity=4
        ),
        ItemQuantity(
            item_id=2,
            quantity=5
        ),
        ItemQuantity(
            item_id=1,
            quantity=2
        )
    ]
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )
    item_ids = [1]
    err  = InvalidDuplicateItem(item_ids)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                        storage=storage
                 )

    storage.vaildate_duplicate_item_ids \
        .side_effect = err
    presenter.raise_exception_for_invalid_duplicate_items_ids \
        .side_effect = InvalidRequestTypeException

    with pytest.raises(InvalidRequestTypeException):
        interactor \
            .order_breakfast_wrapper(order=order,
                                     presenter=presenter)

    storage.vaildate_duplicate_item_ids \
        .assert_called_once_with(items=items)
    presenter.raise_exception_for_invalid_duplicate_items_ids \
        .assert_called_once()