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
                       
    (Pseudocode added by jon)
    Returns: a dict containing:
        a dict named 'operations' with their functions.
        a list named 'history' of tuples. [should initialize empty.]
    """
    if not operations: 
        operations = {}
    return {'operations': operations, 'history': []}


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    # Check to see if the operation exists
    # Enabling this requires enabling the test suite:
    # test_perform_nonexistant_operation
    '''
    if operation not in get_operations(calc):
        raise InvalidOperation('Given operation is invalid.')
    '''
    
    # Check the params
    for num in params:
        if not isinstance(num,(int, float, complex)):
            raise InvalidParams('Given params are invalid.')

    # compute the result
    result =  calc['operations'][operation](*params)
    
    #Update the history with the operation.
    #logentry format: ('2016-05-20 12:00:00', 'add', (1, 2), 3)
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
    logentry = (timestamp, operation, params, result)
    calc['history'].append(logentry)

    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    # first check if we passed the operation as a proper dict.
    if not isinstance(operation, dict):
        raise InvalidOperation('Given operation is invalid.')

    # This is a test to see if the op is a valid function
    # including this requires enabling the test suite:
    # test_add_new_operations_invalid_operation_type_in_dict
    '''
    if not hasattr(list(operation.values())[0], '__call__'):
        raise InvalidOperation('Given operation is invalid.')
    '''
    
    # Replace operations with new operations dict empty, otherwise update dict.
    if not calc['operations']:
        calc['operations'] = operation
    else:
        calc['operations'].update(operation)


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
    # TODO: catch exceptions if history is nonexistant.
    
    if len(calc['history']) == 0:
        return None
    else:    
        # Can break this into separate lines to extract.
        # Or you can make one really long complex hard to read line.
        # or just discard the unused values with the commonly used _.
        _, operation, params, _ = calc['history'][-1]
        return perform_operation(calc, operation, params)
