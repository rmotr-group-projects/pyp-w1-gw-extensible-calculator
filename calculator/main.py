from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations={}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    return { "history": [], "operations": operations}


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    if operation not in calc["operations"]:
        raise InvalidOperation('"{}" operation not supported.'.format(operation))
    
    if params in (True, False):
        raise InvalidParams("Given params are invalid.")
    elif not all([isinstance(param, (float,int)) for param in params]):
        raise InvalidParams("Given params are invalid.")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    result = calc["operations"][operation](*params)
    
    calc["history"].append((now, operation, params, result))
    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if not isinstance(operation, dict) :
        raise InvalidOperation('Given operation is invalid.')
        
    key = list(operation.keys())[0]
    calc["operations"][key] = operation[key]
    return calc


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc["operations"].keys())
        


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    return calc["history"]


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc["history"] = []


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if calc["history"] != []:
        return calc["history"][-1][3]
