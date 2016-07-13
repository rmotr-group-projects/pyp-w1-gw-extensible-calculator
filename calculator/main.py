from datetime import datetime

from .operations import *
from .exceptions import *


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
                       
    """
    
    if operations is not None:
        calculator ={
            'operations':operations,
            'history':[]
        }
        
    else:
        calculator ={
            'operations':{},
            'history':[]
        }
                  
    return calculator


def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator. #JN: Calc is a dictionary with operations
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    # need to add exceptions for: an operation not in calc, invalid parameters, and insufficient parameters

    if operation not in get_operations(calc):
        raise InvalidOperation("Given operation is invalid.")
    for number in params:
        if isinstance(number, str) is True:
            raise InvalidParams("Given params are invalid.")
   
    params_list = list(params)
    function = calc['operations'][operation] #gives us the function name of the operation specified
    datetime_obj = datetime.now()

    result = params[0] 
    for num in params[1:]:
        result = function(num, result)

    
    formatted_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    calc['history'].append((formatted_date, operation, params, result))

    return result
def add_new_operation(calc, operation):
    
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if not isinstance(operation, dict):
        raise InvalidOperation('Given operation is invalid.')
    calc['operations'].update(operation)
    #return calc


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    # """

    return calc['operations'].keys()


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    #every performed actionneeds to call this function
    #format time here, getcurrent time

    return calc['history']


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc['history']=[]
    

def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if calc['history'] == []:
        return None
    return calc['history'][-1][3]

    #return history_list[0]
