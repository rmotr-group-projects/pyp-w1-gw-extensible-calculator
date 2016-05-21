from datetime import datetime
import numbers

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
    calc = {'operations':{}, 'history':[]}
    if operations:
        calc['operations'] = operations
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
    
    # Test parameters, raise error if invalid
    if operation != 'plot':
        valid_params = all(
                [isinstance(param, numbers.Number) for param in params]
            )
        if not valid_params:
            raise InvalidParams('Given params are invalid.')
    
    # Check operation, raise error if invalid
    if operation not in get_operations(calc):
        not_supported = '"{}" operation not supported.'
        raise InvalidOperation(not_supported.format(operation))
    
    # Perform operation
    result = calc['operations'][operation](*params)
    
    # Update history
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history = (now, operation, params, result)
    calc['history'].append(history)
    
    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    
    # Test operation, raise error if invalid
    if not isinstance(operation, dict):
        raise InvalidOperation('Given operation is invalid.')
    if len(operation) != 1:
        raise InvalidParams('Can only add one operation at a time')
    
    # Add operation to calculator
    operation_name, operation_function = next(iter(operation.items()))
    
    calc['operations'][operation_name] = operation_function


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
    if calc['history']:
        return calc['history'][-1][3]
