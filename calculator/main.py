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
    if operations is None:
        return {'operations':{}, 'history':[]}
    else:
        return {'operations':operations, 'history':[]}

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    
    if not all([any([isinstance(item, int), isinstance(item, float)]) for item in params]):
        raise InvalidParams("Given params are invalid.")
    elif operation not in calc['operations']:
        raise InvalidOperation("operation not supported.")
    else:
        result = calc['operations'][operation](*params)
        calc['history'].append((str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),operation, params, result))
        return result

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if operation != plot and type(operation) is not dict:
        raise InvalidOperation('Given operation is invalid.')
    elif type(operation) is dict: 
        calc['operations'].update(operation)
    else:
        calc['operations']['plot'] = plot


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'].keys())


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
    if len(calc['history']) == 0:
        return None
    op = calc['history'][-1][1]
    params = calc['history'][-1][2]
    return perform_operation(calc, op, params)
