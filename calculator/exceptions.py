
class InvalidOperation(Exception):
    def __init__(self, operation):
        self.operation = operation
        if (self.operation == 1):
            Exception.__init__(self, 'Given operation is invalid.')
        else:
            Exception.__init__(self, '"{}" operation not supported.'.
                           format(self.operation))


class InvalidParams(Exception):
    def __init__(self):
        Exception.__init__(self, 'Given params are invalid.')
