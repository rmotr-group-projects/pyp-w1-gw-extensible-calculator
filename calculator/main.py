from __future__ import division
from datetime import datetime
from calculator.operations import *
from calculator.exceptions import *

def create_new_calculator(operations={}):
#def create_new_calculator(operations={'add':add,'subtract':subtract,'multiply':multiply,'divide':divide}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """

    my_operations={}
    for key in operations:
        my_operations[key] = operations[key]
    
    calc = {
        'operations':my_operations,
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
    my_operation = calc['operations'][operation]
    try:
        result = my_operation(*params)
    except KeyError:
        raise InvalidOperation('Given operation is invalid.')
    except TypeError:
        raise InvalidParams('Given params are invalid.')
    
    
    ## add history entry to calc
    now = str(datetime.now())
    calc['history'].append((now,operation,params,result))

    return result

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    
    #calc['operations'] = dict(list(calc['operations'].items()) + list(operation.items()))
    
    if isinstance(operation, dict) == True:
        newname = list(operation.keys())[0]
        newval = operation[newname]
        calc['operations'][newname] = newval
        return calc
    else:
        raise InvalidOperation('Given operation is invalid.')


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
    return calc


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    #'perform_operation(calc, operation, params)'
    if calc['history'] != []:
        operation = calc['history'][-1][1]
        params = calc['history'][-1][2]
        #operation = calc['operations'][operation]
        return perform_operation(calc,operation,params)
    return None
    
""" debug
    Returns the result of the last operation executed in the history.
    
    #'perform_operation(calc, operation, params)'
    operation = calc['history'][-1][1]
    print("my operation is {}".format(operation))
    params = calc['history'][-1][2]
    print("my params is {}".format(params))
    operation = calc['operations'][operation]
    print("my operation is {}".format(operation))
    return perform_operation(calc,operation,*params)
"""
    
