from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations={}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    new_calculator = {
        'operations': operations,
        'history': []
    }
    return new_calculator
        
    
def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    dtnow = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    
    if operation not in calc['operations']:
         raise InvalidOperation("Given operation is invalid.")
    
    if isinstance(params, tuple):
        for v in params:
            if not isinstance(v, float) and not isinstance(v, int):
                    raise InvalidParams("Given params are invalid.")
        
    result = calc['operations'][operation](*params)
    #calc["history"].append(dtnow,operation,params)
    
    calc['history'].append( 
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        operation, params, result
        )
    )

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
    
    for key,value in operation.items():
        calc['operations'][key] = value

    return calc
    
    


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """

    return list(calc.get('operations'))



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
    # if len(calc['history']) == 0:
    #     return
    
    if calc['history'] == []:
        return None
        
    return calc['history'][-1][3]
