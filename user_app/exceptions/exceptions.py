class InvalidUsername(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidUserId(Exception):

    def __init__(self, invalids):
        self.invalids = invalids