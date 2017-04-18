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
        return {
            'operations' : {},
            'history' : []
        }
    #return dict([('operations', {k : v for k, v in operations.iteritems()}), 
               #('history', [])])
    return {
        'operations' : operations,
        'history': []
    }

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    return: result of the operation
    """
    
    if not all([isinstance(param, (int, float)) for param in params]):
        raise InvalidParams("Given params are invalid.")

    if operation in calc['operations'].keys():
        result = calc['operations'][operation](*params)
        _add_history_entry(calc, operation, params, result)
        return result
    else:
        raise InvalidOperation

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if not isinstance(operation, dict):
        raise InvalidOperation('Given operation is invalid.')
    if list(operation.keys())[0] not in calc['operations'].keys():
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
    """
    Resets the calculator history back to an empty list.
    """
    calc['history'] = []

def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if len(calc['history']) != 0:
        return calc['history'][-1][-1]
    
#Helper functions

def _add_history_entry(calc, operation, params, result):
    """
    adds an entry into the history
    """
    ts = datetime.now()
    date_time = ts.strftime('%Y-%m-%d %H:%M:%S')
    new_history_entry = (date_time, operation, params, result)
    calc['history'].append(new_history_entry)
