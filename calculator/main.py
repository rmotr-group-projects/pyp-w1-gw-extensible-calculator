from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *

from time import gmtime, strftime


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    if operations == None:
        operations = {}
    
    calc = {
        'operations': operations,
        'history': []
    }
                
    return calc 
    pass


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    list_of_operations = calc['operations']
    
    
    #Isnt raising the value error first less efficient? The loop is looking for the operation so its going to check the entire list. Where as if we handle the case that it is there
    # it will stop if the operation is present before the end of the list
    try:
        if operation not in list_of_operations:  
            raise InvalidOperation('Invalid Operation')    
        else:
            date = strftime("%Y-%m-%d %H:%M:%S")
            result = calc['operations'][operation](*params)
            calc['history'].append((date, operation, params, result))
            return result
            #[operation](params) 
    except TypeError:
        raise InvalidParams(TypeError)
 

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    #aDict[key] = value
    
    # key = operation.keys()[0]
    # calc['operations'][key] = operation[key]
    try:
     return calc['operations'].update(operation)
    except ValueError:
        raise InvalidOperation(ValueError)
    pass
    


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'].keys())
    pass


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    if calc['history'] == []:
        return []
    return calc['history']
    pass


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    del calc['history'][:]
    calc['history'] = []
    return calc['history']
    pass


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    #calc['history'].append([datetime.datetime.now(), operation, params, result])
    #if calc['history'] == []:
       # raise InvalidOperation('history cannot be empty')
    
    for i, item in enumerate(calc['history']):
        if i > 0:
            last_execution = calc['history'][i]
            return perform_operation(calc, last_execution[1], last_execution[2])
    pass

#print calc["operations"]