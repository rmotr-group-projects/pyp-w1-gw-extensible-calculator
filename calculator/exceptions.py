
class InvalidOperation(Exception):
    def __init__(self):
        Exception.__init__(self,'Given operation is invalid.')


class InvalidParams(Exception):
    def __init__(self):
        Exception.__init__(self,'Given params are invalid.')
