import time

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
    calc = {'history':[],'operations':{}}
    if operations is not None:
        calc['operations'].update(operations)
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
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = calc['operations'][operation](*params)
    except KeyError:
        raise InvalidOperation('"{}" operation not supported.'.format(operation))
    except ValueError:
        raise InvalidParams('Given params are invalid.')
    except TypeError:
        raise InvalidParams('Given params are invalid.')
    calc['history'].append((now, operation, params, res))
    return res


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    try:
        calc['operations'].update(operation)
    except ValueError:
        raise InvalidOperation('Given operation is invalid.')


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'])


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.
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
    hist = calc['history']
    if hist:
        return hist[-1][-1]