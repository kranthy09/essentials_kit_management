class InvalidOffSet(Exception):
    pass

class InvalidLimit(Exception):
    pass


class OrderedItemDoesNotExist(Exception):
    pass

class UniqueItemException(Exception):

    def __init__(self, duplicates):
        self.duplicates = duplicates

class InvalidItem(Exception):

    def __init__(self, invalids):
        self.invalids = invalids

class UniqueSectionException(Exception):

    def __init__(self, duplicates):
        self.duplicates = duplicates

class InvalidSectionId(Exception):

    def __init__(self, invalids):
        self.invalids = invalids

class InvalidForm(Exception):
    pass
