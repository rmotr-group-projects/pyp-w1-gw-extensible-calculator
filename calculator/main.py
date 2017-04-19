from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *
from calculator.utility import *

def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    calc = {}
    if(operations == None):
        operations = {}
    validate(operations, dict, InvalidOperation, operation_error_msg)
    calc['operations'] = operations
    calc['history'] = []
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
    validate(operation, str, InvalidOperation, operation_error_msg)
    validate_params(params, tuple, InvalidParams, param_error_msg)
    func = calc["operations"][operation]
    ans = func(*params)
    time = get_current_time_str()
    add_history(calc, time, operation, params, ans)
    return ans


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    validate(operation, dict, InvalidOperation, operation_error_msg)
    operations = calc["operations"]
    operation_tuple = operation.popitem()
    operation_name = operation_tuple[0]
    operation_function = operation_tuple[1]
    operations[operation_name] = operation_function
    #print (operations)
    pass


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    validate(calc, dict, Exception, "")
    operation_dicitionary = calc["operations"]
    return list(operation_dicitionary.keys())
    



def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    validate(calc, dict,Exception, input_error_msg)
    history = calc["history"]
    for item in history:
            print(item)
    return history


def reset_history(calc):
    """
    Resets the calculator history back to an empty list."""
    
    validate(calc, dict, Exception, "")
    while len(calc["history"]) != 0:
        calc["history"].pop()
    pass


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    eq: ('2016-05-20 12:00:00', 'add', (1, 2), 3)
    """
    validate(calc, dict, Exception, input_error_msg)
    history = calc["history"]
    if len(history) == 0:
        return None
    old_result = history[-1]
    return old_result[3]
    
    pass

def add_history(calc, time, operation_name, params, result):
    """
    add an item in history list of the calculator
    an history element is a tuple:
        eq: ('2016-05-20 12:00:00', 'add', (1, 2), 3)
    """
    history_list = calc["history"]
    history = (time, operation_name, params, result)
    history_list.append(history)
    pass