from typing import List

class InvalidPostId(Exception):
    pass

class InvalidItemId(Exception):

    def __init__(self, item_ids):
        self.item_ids = item_ids

class InvalidMealId(Exception):
    pass

class ItemNotFound(Exception):

    def __init__(self, items_not_in_meal):
        self.items_not_in_meal = items_not_in_meal

class InvalidItemQuantity(Exception):

    def __init__(self, items_with_quantity_limit_exceeded: List[int]):
        self.items_with_quantity_limit_exceeded \
            = items_with_quantity_limit_exceeded

class InvalidDate(Exception):
    pass

class InvalidOrderTime(Exception):
    pass

class InvalidDuplicateItem(Exception):

    def __init__(self, item_ids):
        self.item_ids = item_ids





















































































