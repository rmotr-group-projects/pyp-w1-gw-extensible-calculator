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

    calc = {
            'operations': {},
            'history': []
        }
    if operations:
        calc['operations'] = operations
    return calc


def perform_operation(calc, operation, params=None):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
   
    # Allow each parameter is int or float, but not if bool.
    if not all(isinstance(p, (int, float)) for p in params if not isinstance(p, bool)):
        raise(InvalidParams('Given params are invalid.'))
    
    
    # If operation is not in operations dictionary, deny.
    if not operation in calc["operations"]:
        raise(InvalidOperations('{} not supported'.format(operation)))
    
    
    # Pass parameters to lambda stored in operations dictionary.
    result = calc["operations"][operation](*params)
    
    
    # Obtain date and save to history dictionary.
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = (date, operation, params, result)
    calc['history'].append(entry)
    
    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    
    # Deny if passed operation is in required Dictionary format.
    if not isinstance(operation, dict):
	    raise InvalidOperation("Given operation is invalid.")
    
    # Add new operation to operations Dictionary.
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
    
    # If History key in calc Dictionary has content, rerun last operation.
    if calc['history']:
        operation = calc['history'][-1][1]
        params = calc['history'][-1][2]
        return calc["operations"][operation](*params)
    else:
        return None