class InvalidPostId(Exception):
    pass

class InvalidDomainId(Exception):
    pass

class InvalidUserIdInDomain(Exception):
    pass

class InvalidOffset(Exception):
    pass

class InvalidLimit(Exception):
    pass

class InvalidPostIds(Exception):
    def __init__(self, post_ids):
        self.post_ids = post_ids

class UniquePostIdException(Exception):
    def __init__(self, duplicates):
        self.duplicates = duplicates

class InvalidPostIdException(Exception):
    def __init__(self, invalids):
        self.invalids=invalids
