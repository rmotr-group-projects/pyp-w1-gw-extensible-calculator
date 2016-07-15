from datetime import datetime
from time import time

from calculator.operations import *
from calculator.exceptions import *
from pprint import pprint as soFabulous

def create_new_calculator(operations={}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ..}.
    """
    if check_integrity(operations, check_calc=False):
        return { 'operations' : operations, 'history' : [] }

def check_integrity(calculator, check_calc=True):
    """
    If calculator is a new calculator, check if operations is a dictionary
    Check if calculator is a dictionary
    Check if calculator has operations and history in it
    """
    try:
        if not isinstance(calculator, dict):
            raise CalculatorError()
        elif check_calc and ('operations' not in calculator or 'history' not in calculator):
            raise CalculatorError()
        else:
            return True
    except CalculatorError as err:
        print err.invalid_calc
        return False

def check_arguments_for_error(argument, error_type):
    try:
        argument
    except error_type as error:
        raise error.error_msg
        return True
    else:
        return False

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    if check_integrity(calc):
        # check to see if operation parameter exists within calculator object
        if operation not in calc['operations']:
            raise InvalidOperation('Given operation is invalid.') #This is hardcoded, fix this
        else:
            if all([isinstance(parameter, (int, float)) for parameter in params]):
                result = calc['operations'][operation](*params)
                dt = datetime.strftime(datetime.fromtimestamp(time()), '%Y-%m-%d %H:%M:%S')
                calc['history'].append((dt, operation, params, result))
                print result
                return result
            else:
                raise InvalidParams('Given params are invalid.') #This is hardcoded, fix this

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if check_integrity(calc):
        if check_integrity(operation, check_calc=False):
            for operand in operation:
                if operand not in calc['operations']:
                    calc['operations'][operand] = operation[operand]
                else:
                    print 'Skipping %s: %s exist in calculator.' % (operand, operand)
        else:
            raise InvalidOperation('Given operation is invalid.') #This is hardcoded, fix this

def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    if check_integrity(calc):
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
    if check_integrity(calc):
        return calc['history']


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    # check to see if calc exists
    if check_integrity(calc):
        del calc['history'][:]


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if check_integrity(calc):
        # print the most recent entry in history
        # the 3th entry in the tuple is the result of the operation.
        if len(calc['history']) > 0:
            return calc['history'][-1][3]
        else:
            return None