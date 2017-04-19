
class InvalidOperation(Exception):
    def __init__(self, operation):
        self.operation = operation
        if (self.operation == 1):
            super(InvalidOperation, self).__init__('Given operation is invalid.')
        else:
            super(InvalidOperation, self).__init__('"{}" operation not supported.'.
                           format(self.operation))


class InvalidParams(Exception):
    def __init__(self):
        super(InvalidParams, self).__init__('Given params are invalid.')
