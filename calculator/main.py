from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *

from functools import *


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    return { 'operations': (operations if operations is not None else {}), 'history':[] }


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    if operation not in calc['operations'].keys():
        raise InvalidOperation("Given operation is invalid")
    if not all([isinstance(param, float) or isinstance(param, int) for param in params]):
        raise InvalidParams("Given params are invalid.")

    result = reduce(calc['operations'][operation], [float(x) for x in params])

    op_time = datetime.now()
    op_time_str = '{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'.format(op_time.year, op_time.month, op_time.day,
                                                                       op_time.hour, op_time.minute, op_time.second)
    calc['history'].append((op_time_str, operation, params, result))
    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if not isinstance(operation, dict):
        raise InvalidOperation("Given operation is invalid.")
    calc['operations'][list(operation.keys())[0]] = list(operation.values())[0]


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
    calc['history'] = []


def repeat_last_operation(calc):
    if not calc['history']:
        return None
    return calc['history'][-1][-1]
