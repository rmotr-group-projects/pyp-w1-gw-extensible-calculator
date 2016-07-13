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
    calculator = {'operations': operations, 'history':[]}
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
    for param in params:
        if type(param) not in [int,float]:
            raise InvalidParams("Given params are invalid.")
    if operation in calc['operations']:
        # get the operation
        op = calc['operations'][operation]
        # split out the params
        param_list = []
        for x in params:
            param_list.append(x)
        # do the calculation
        result = op(*param_list)
        
        #construct the history entry
        #first, get the time now
        time_now = str(datetime.now())
        transaction = (time_now, operation, params, result)
        # add the history entry
        calc['history'].append(transaction)
        
        return(result)
        
    else:
        raise InvalidOperation("Operation not supported")
    


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    # Check validity of operation.
    if type(operation) != dict:
        raise InvalidOperation("Given operation is invalide.")
    calc['operations'].update(operation)


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


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    # Check if the history is empty
    if calc['history']:
        # Get the last history entry and bits from it we need
        latest_index = len(calc['history'])-1
        latest_history_entry = calc['history'][latest_index]
        latest_operation = latest_history_entry[1]
        latest_params = latest_history_entry[2]
        
        result = perform_operation(calc, latest_operation, latest_params)
        return(result)
    else:
        return None