import pytest
import datetime
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import (NotFound,
            BadRequest)
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

def test_order_item_interactor_with_invalid_item_ids():

    # Arrange
    meal_id = 5
    date = datetime.datetime(2020, 9, 12, 12, 30, 12)
    order_time = datetime.datetime(2020, 9, 12, 12, 30, 12)
    order_deadline_time = datetime.datetime(2020, 9, 12, 9, 00, 00)
    items = [
        ItemQuantity(
            item_id=-1,
            quantity=4
        ),
        ItemQuantity(
            item_id=-2,
            quantity=5
        ),
        ItemQuantity(
            item_id=3,
            quantity=5
        )
    ]
    meal_valid_date = datetime.datetime(2020, 9, 12, 12, 30, 12)
    meal_items = [-1, -2, 3]
    item_ids = [item.item_id for item in items]
    all_item_in_storage = [3, 5, 6]
    invalid_item_ids = [-1, -2]
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
    storage.validate_meal_id \
        .return_value = None
    storage.validate_item_ids \
        .return_value = all_item_in_storage
    presenter.raise_exception_for_invalid_item_ids \
        .side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor \
            .order_breakfast_wrapper(order=order,
                                     presenter=presenter)
    storage.validate_meal_id \
        .assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids \
        .assert_called_once_with(item_ids=item_ids)
    err = presenter.raise_exception_for_invalid_item_ids \
        .call_args.kwargs['item_ids']
    assert err.item_ids == invalid_item_ids

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
    meal_items = [1,3,4]
    all_item_in_storage = [1, 2, 4]
    item_ids = [item.item_id for item in items]
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
    items_not_in_meal = [2]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                    storage=storage
                 )
    storage.validate_meal_id.side_effect = None
    storage.validate_item_ids.return_value = all_item_in_storage
    storage.validate_items_in_meal_id.return_value = meal_items
    presenter.raise_exception_for_item_not_found \
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.order_breakfast_wrapper(
                order=order,
                presenter=presenter
            )
    err = presenter.raise_exception_for_item_not_found.call_args.kwargs['items_not_in_meal']
    storage.validate_meal_id.assert_called_once()
    storage.validate_item_ids.assert_called_once_with(item_ids=item_ids)
    storage.validate_items_in_meal_id \
        .assert_called_once_with(items=items,
                                 meal_id=meal_id)
    presenter.raise_exception_for_item_not_found.assert_called_once()
    assert err.items_not_in_meal == items_not_in_meal

def test_order_item_interactor_item_invalid_quantity():

    # Arrange
    meal_id = 4
    request_items = [
        ItemQuantity(
            item_id=1,
            quantity=-5
        ),
        ItemQuantity(
            item_id=4,
            quantity=6
        ),
        ItemQuantity(
            item_id=6,
            quantity=-6
        )
    ]
    date = "2020-4-9"
    order_time="9:34:21"
    order_deadline_time = "7:00:00"
    order = OrderDto(
                meal_id=meal_id,
                date=date,
                items=request_items,
                order_time=order_time,
                order_deadline_time=order_deadline_time
            )
    items_with_invalid_quantity = [1,6]
    meal_items = [1,4,6]
    item_ids = [item.item_id for item in request_items]
    all_items_in_storage = [1,4,6]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = OrderBreakFastInteractor(
                    storage=storage
                 )
    storage.validate_meal_id.return_value = None
    storage.validate_item_ids.return_value = all_items_in_storage
    storage.validate_items_in_meal_id.return_value = meal_items
    presenter.raise_exception_for_item_quanity_limit_reached \
        .side_effect = BadRequest
    # Act
    with pytest.raises(BadRequest):
        interactor \
            .order_breakfast_wrapper(order=order,
                                     presenter=presenter)
    storage.validate_meal_id \
        .assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids \
        .assert_called_once_with(item_ids=item_ids)
    storage.validate_items_in_meal_id \
        .assert_called_once_with(items=request_items, meal_id=meal_id)
    err = presenter.raise_exception_for_item_quanity_limit_reached \
        .call_args.kwargs['items']
    assert err.items == items_with_invalid_quantity

def test_order_item_interactor_with_invalid_order_date():

    # Arrange
    
    meal_id = 5
    date = datetime.datetime(2020, 9, 5)
    order_time = "10:34:11"
    order_deadline_time = "7:00:00"
    items = [
      ItemQuantity(
        item_id = 1,
        quantity = 4
      ),
      ItemQuantity(
        item_id = 2,
        quantity = 5
      ),
      ItemQuantity(
        item_id = 3,
        quantity = 2
      )
    ]
    meal_valid_date = datetime.datetime(2020, 8, 6)
    order = OrderDto(
      meal_id = meal_id,
      date = date,
      items = items,
      order_time = order_time,
      order_deadline_time = order_deadline_time
    )
    meal_items = [1,2,3]
    all_items_in_storage = [1,2,3]
    item_ids = [item.item_id for item in items]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    
    interactor = OrderBreakFastInteractor(
      storage = storage
    )
    storage.validate_meal_id.return_value = None
    storage.validate_item_ids.return_value = all_items_in_storage
    storage.validate_items_in_meal_id.return_value = meal_items
    storage.validate_order_date \
      .return_value = meal_valid_date
    presenter.raise_exception_for_invalid_order_date \
      .side_effect = BadRequest
    
    # Act
    with pytest.raises(BadRequest):
      interactor.order_breakfast_wrapper(
        order = order,
        presenter = presenter
      )
    storage.validate_meal_id \
        .assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids \
        .assert_called_once_with(item_ids=item_ids)
    storage.validate_order_date \
      .assert_called_once_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_order_date \
      .assert_called_once()

def test_order_item_interactor_with_order_in_right_time():

    # Arrange
    meal_id = 5
    date = datetime.datetime(2020, 9, 12, 12, 30, 12)
    order_time = datetime.datetime(2020, 9, 12, 12, 30, 12)
    order_deadline_time = datetime.datetime(2020, 9, 12, 9, 00, 00)
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
    meal_valid_date = datetime.datetime(2020, 9, 12, 12, 30, 12)
    meal_items = [1,2]
    item_ids = [item.item_id for item in items]
    all_items_in_storage = [1,2]
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
    storage.validate_meal_id.return_value = None
    storage.validate_item_ids.return_value = all_items_in_storage
    storage.validate_items_in_meal_id.return_value = meal_items
    storage.validate_order_date.return_value = meal_valid_date
    storage.validate_ordered_in_right_time \
        .return_value = order_deadline_time
    presenter.raise_exception_for_invalid_order_time \
        .side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.order_breakfast_wrapper(
                        order=order,
                        presenter=presenter
                  )
    storage.validate_meal_id \
        .assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids \
        .assert_called_once_with(item_ids=item_ids)
    storage.validate_ordered_in_right_time \
        .assert_called_once_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_order_time \
        .assert_called_once()

# def test_order_item_interactor_with_invalid_duplicate_item_ids():

#     # Arrange
#     meal_id = 5
#     date = "2020-9-5"
#     order_time = "10:34:11"
#     order_deadline_time = "7:00:00"
#     items = [
#         ItemQuantity(
#             item_id=1,
#             quantity=4
#         ),
#         ItemQuantity(
#             item_id=2,
#             quantity=5
#         ),
#         ItemQuantity(
#             item_id=1,
#             quantity=2
#         )
#     ]
#     order = OrderDto(
#                 meal_id=meal_id,
#                 date=date,
#                 items=items,
#                 order_time=order_time,
#                 order_deadline_time=order_deadline_time
#             )
#     item_ids = [1]
#     err  = InvalidDuplicateItem(item_ids)
#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     interactor = OrderBreakFastInteractor(
#                         storage=storage
#                  )

#     storage.vaildate_duplicate_item_ids \
#         .side_effect = err
#     presenter.raise_exception_for_invalid_duplicate_items_ids \
#         .side_effect = BadRequest

#     with pytest.raises(BadRequest):
#         interactor \
#             .order_breakfast_wrapper(order=order,
#                                      presenter=presenter)

#     storage.vaildate_duplicate_item_ids \
#         .assert_called_once_with(items=items)
#     presenter.raise_exception_for_invalid_duplicate_items_ids \
#         .assert_called_once()