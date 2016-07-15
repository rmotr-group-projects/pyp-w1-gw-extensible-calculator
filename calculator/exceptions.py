class InvalidOperation(Exception):
    def __init__(self):
        Exception.__init__(self,"Given operation is invalid.") 

class InvalidParams(Exception):
    def __init__(self):
        Exception.__init__(self,"Given params are invalid.") 

class CalculatorError(Exception):
    """docstring for NoCalculator"""
    def __init__(self):
        self.invalid_calc = "NoCalculator: Calculator does not exist"
        self.invalid_param = 'InvalidParams: Calculator params are invalid.'