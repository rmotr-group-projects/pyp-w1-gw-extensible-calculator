from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    
    # Initialize calc
    calc = {}
    calc['history'] = []
    calc['operations'] = {}
    
    # If there are operations, add to dictionary
    if operations:
        for key, value in operations.items():
            calc['operations'][key] = value
    
    return calc


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    
    # ADD CODE TO RAISE InvalidOperation
    
    # Check parameter validity
    if len(params) == 0:
        raise InvalidParams("Given params are invalid.")
    for arg in params:
        if not (type(arg) == int or type(arg) == float):
            raise InvalidParams("Given params are invalid.")
                
    function = calc['operations'][operation]

    # Add tuple to history of format: ('2016-05-20 12:00:00', 'add', (1, 2), 3))
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    l = [now, operation]
    
    result = function(*params)
    
    l.append(params)
    l.append(result)
    t = tuple(l)
    calc['history'].append(t)
    
    return result
    

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    
    if type(operation) == dict:
        for key, value in operation.items():
            calc['operations'][key] = value
        return calc
    else:
        raise InvalidOperation("Given operation is invalid.")


def get_operations(calc):
    
    """
    Returns the list of operation names supported by given calculator.
    """

    return list((calc['operations']).keys())


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    
    history = []
    
    for item in calc['history']:
        history.append(item)
    
    return history


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    
    calc['history'] = []
    
    pass


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    
    if calc['history']:
        previous_tuple = calc['history'][-1]
        operation = previous_tuple[1]
        params = previous_tuple[2]
        result = perform_operation(calc, operation, params)
        return result
    else:
        return None
