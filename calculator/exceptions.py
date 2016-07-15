class InvalidOperation(Exception):
    pass
    """
    def __init__(self, operation):
        self.error_msg = 'Given operation is invalid.'
    """

class InvalidParams(Exception):
    """
    def __init__(self):
        self.error_msg = 'Given params are invalid.'
    """
    pass

class CalculatorError(Exception):
    """docstring for NoCalculator"""
    def __init__(self):
        self.invalid_calc = "NoCalculator: Calculator does not exist"
        self.invalid_param = 'InvalidParams: Calculator params are invalid.'