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
    """

    
    calc = {
            'operations': operations,
            'history': []
        }
    
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
    
    try:
        result = calc['operations'][operation](*params)
    except KeyError: #key not in dictionary
        raise InvalidOperation('Given operation is invalid.')
    except TypeError:
        raise InvalidParams('Given params are invalid.')
        
    #add to history ('2016-05-18 12:00:00', 'add', (1, 2, 3, 4), 10), 
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    calc['history'].append((time, operation, params, result))
    
    return result
    
    '''
    op = 'add'
    if op in operations:
        op_function = operations[op]
    else:
        raise InvalidOperation
    '''
    


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    
    for key, value in operation.items():
        calc['operations'][key] = value
    
    return calc


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return calc['operations'] #?


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    
    return calc['history'] #
    


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    
    calc['history'] = []
    return calc


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    
    if calc['history'] == []:
        return None
    return calc['history'][-1][1]
