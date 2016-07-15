from datetime import datetime
from collections import defaultdict
import datetime
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
    current_calc = defaultdict()
    current_calc['operations'] = {}
    current_calc['history'] = []
    if operations : 
        current_calc['operations'] = dict(operations)
    
    return current_calc     
    

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.
    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
        
    if operation not in calc['operations'] :
        raise InvalidOperation(operation, "operation not supported.")
        
    for num in params:
        if not isinstance(num, int) and not isinstance(num, float):
            raise InvalidParams('Given params are invalid.')
    
    to_do = calc['operations'][operation]
    try : 
        answer = to_do(*params)
    except AttributeError :
        raise InvalidParams('Given params are invalid.')
    
    dt = datetime.datetime.now()
    date_and_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    operation_history = (date_and_time, operation, params, answer)
    calc['history'].append(operation_history)
    
    return answer
    

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    try :
        calc['operations'].update(operation)
    except :
        raise InvalidOperation("Given operation is invalid.")

def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    current_operations = []
    
    for k in calc['operations']:
        current_operations.append(k)
    
    return current_operations
    

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
    if calc['history'] == [] :
        return None
    else :    
        return calc['history'][-1][-1]