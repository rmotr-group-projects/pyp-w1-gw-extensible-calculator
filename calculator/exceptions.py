
class InvalidOperation(Exception):
    def __init__(self, message):
        super(InvalidOperation, self).__init__(message)
        pass

class InvalidParams(Exception):
    def __init__(self, message):
        super(InvalidParams, self).__init__(message)
        pass

param_error_msg = "Given params are invalid."
operation_error_msg = "Given operation is invalid."
input_error_msg = "Given input is invalid."