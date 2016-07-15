from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *

def create_new_calculator(operations={}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    calculator_dict = {'operations':operations,'history':[]}
    return calculator_dict
    
def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                  ie: (1, 2, 3, 4.5, -2)
    """
    if operation not in calc['operations']:
        raise InvalidOperation("Given operation is invalid.")
    for item_in_params in params:
        print(type(item_in_params))
        if type(item_in_params) != int and type(item_in_params) != float:
            raise InvalidParams("Given params are invalid.")
            
    operation_name = calc['operations'][operation]
    result = operation_name(*params)
    calc['history'].append((datetime.today().strftime('%Y-%m-%d %H:%M:%S'), operation, params, result))
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
    for key in operation:
        calc['operations'][key] = operation[key]

def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'])

def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    return list(calc['history'])

def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc['history']= []

def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if calc['history'] == []:
        return None
    else:
        return perform_operation(calc,*get_history(calc)[-1][1:3])