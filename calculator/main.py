from datetime import datetime
from collections import namedtuple
from calculator.operations import *
from calculator.exceptions import *

history_rec = namedtuple('HistoryRecord','event_time,operation,params,result')

def create_new_calculator(operations={}):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    calc = {'operations':operations,'history':[]}
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
    if not isinstance(params,tuple) or len(params)==0:
        raise InvalidParams("Given params are invalid.")
    if operation in calc['operations']:
        try:
            func = calc['operations'][operation]
            result = func(*params)
            add_history(calc,operation,params,result)
            return result
        except:
            raise InvalidParams("Given params are invalid.")
    else:
        raise InvalidOperation("'{0}' not supported".format(operation))

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if isinstance(operation,dict):
        calc['operations'].update(operation)
    else:
        raise InvalidOperation("Given operation is invalid.")


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
    calc['history']=[]


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    last_op=None
    if len(calc['history'])>0:
        last_op = calc['history'][-1].result
    return last_op

def add_history(calc,operation,params,result):
    """
    Adds history record for calculator passed
    in the following format.
    
    ('2016-05-18 12:00:00', 'add', (1, 2, 3, 4), 1)
    """
    hr = history_rec(event_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    operation=operation,
                    params=params,
                    result=result)
    calc['history'].append(hr)