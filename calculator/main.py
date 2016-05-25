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
    if len(params)<1:
        raise InvalidParams('Given params are invalid.')
    if operation not in calc['operations']:  
        raise InvalidOperation(operation + " operation not supported.")
    float_params = [float(num) for num in params] #necessary?
        
    func = calc['operations'][operation] 
    result = func(params)
    current = datetime.now()
    format_time = current.strftime("%Y-%m-%d %X")
    #time.strftime(format[%Y-%m-%d %X])
    #2016-05-18 12:00:00
    #time.strftime("%b %d %Y %H:%M:%S"
    calc['history'].append((format_time, operation, params, result))
    return answer

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    return calc['operations'].update(operation)


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
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
    try: 
        return calc['history'][-1]
    except:
        raise InvalidParams('Given params are invalid.')
        


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc['history'] = []



def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    #makes a list of 2
    try:
        last_op, last_params = calc['history'][-1][1], calc['history'][-1][2]
        return perform_operation(calc, last_op, last_params)
    except:
        if calc['history'] == []:
            return None
        else:    
            raise InvalidParams('Given params are invalid.')

