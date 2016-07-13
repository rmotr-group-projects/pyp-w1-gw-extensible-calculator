from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    if operations is None:
        operations = {}
    
    calculator = {
        "operations" : operations,
        "history" : []
    }
    return calculator


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    if _operation_is_not_valid(calc, operation):
        raise InvalidOperation("Given operation not supported.")
    
    for var in params:
        if isinstance(var, str):
            raise InvalidParams("Given params are invalid.")
        
    answer = calc['operations'][operation](*params)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calc["history"].append((time, operation, params, answer))
    return answer 
    

def _operation_is_not_valid(calc, operation):
    return True if operation not in calc["operations"] else False
    
    
def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    operationIsNotDictionary = not isinstance(operation, dict)
    
    if operationIsNotDictionary:
        raise InvalidOperation("Given operation is invalid.")
        
    for key,value in operation.items():
        calc["operations"][key] = value
   
   
def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    listOfOperations = list(calc["operations"].keys())
    return listOfOperations
        

def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    return calc['history']
    

def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc['history'] = []


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    return None if calc["history"] == [] else calc['history'][-1][3]
