class InvalidPostId(Exception):
    pass

class InvalidItemId(Exception):

    def __init__(self, item_ids):
        self.item_ids = item_ids

class InvalidMealId(Exception):
    pass

class ItemNotFound(Exception):
    pass

class ItemQuantiyLimitReached(Exception):
    pass

class InvalidDate(Exception):
    pass

class InvalidOrderTime(Exception):
    pass

class InvalidDuplicateItem(Exception):

    def __init__(self, item_ids):
        self.item_ids = item_ids