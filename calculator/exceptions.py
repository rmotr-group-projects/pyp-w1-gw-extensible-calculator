class InvalidOperation(Exception):
    def __init__(self, operation):
        self.error_msg = 'InvalidOperation: ' + str(invalid_operation) + 'operation not supported.'


class InvalidParams(Exception):
    def __init__(self):
        self.error_msg = 'InvalidParams:  Given params are invalid.'