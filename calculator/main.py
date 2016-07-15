from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations=None):
    calc = {'operations' : {}, 'history' : []}
    if operations:
        calc['operations'] = operations
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    return calc


def perform_operation(calc, operation, params):
    if operation not in calc['operations']:
        raise InvalidOperation("Given operation is invalid.")
    try:
        result = calc['operations'][operation](*params)
    except:
        raise InvalidParams("Given params are invalid.")

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    calc['history'].append((now,operation,params,result))
    return result
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    


def add_new_operation(calc, operation):
    try:
        calc['operations'].update(operation) # appends the new operation to the current ones
    except:
        raise InvalidOperation("Given operation is invalid.")
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    pass


def get_operations(calc):
    return [operation for operation in calc['operations']]
        

def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3)
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
    if not calc['history']:
        return None
    return calc['history'][-1][3]
