from datetime import datetime
from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(**kwargs):
    calculator = {}
    if kwargs:
        for key, value in kwargs.items():
             calculator[key]=value
    else:
        calculator['operations']={}
    calculator['history'] = []    
    return calculator
    

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
   
    types_of_params = [type(param) == int or type(param) == float for param in params]
    if not all(types_of_params):
        raise InvalidParams('Given params are invalid.')
    current = datetime.now()
    format_time = current.strftime("%Y-%m-%d %I:%M:%S")
    result= calc['operations'][operation](*params)
    calc['history'].append((format_time, operation, params, result))
    return result
    

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if type(operation) != dict:
        raise InvalidOperation("Given operation is invalid.")
    for key, val in operation.items():
        calc['operations'][key]=val
    return calc


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return [op for op in calc['operations'].keys()]


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
    try:
        last_op, last_params = calc['history'][-1][1], calc['history'][-1][2]
        return perform_operation(calc, last_op, last_params)
    except:
        if calc['history'] == []:
            return None
        else:    
            raise InvalidParams('Given params are invalid.')

