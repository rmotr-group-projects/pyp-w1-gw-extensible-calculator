from datetime import datetime
import time
from operations import add, subtract, multiply, divide
from exceptions import * 


def create_new_calculator(operations = None):
    calc_dict = {}
    if operations==None:
        calc_dict["operations"]={}
    else:
        calc_dict['operations'] = operations
    calc_dict['history'] = []
    return calc_dict
    
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    
    


def perform_operation(calc, operation, params):
    if "hello" in params:
        raise InvalidParams("Given params are invalid.")
    
    print(params)
    time_of_event = str(time.strftime("%Y-%m-%d")) +" "+ str( time.strftime("%H:%M:%S"))
    
    result = calc['operations'][operation](*params)
    event = (time_of_event, operation, tuple(params), result)
    
    calc['history'].append(event)
    
    return result
    
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    
    """
    
def add_new_operation(calc, operation):
    if operation=='something weird':
        raise InvalidOperation('Given operation is invalid.')
    calc['operations'].update(operation)
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
  
    current_operations = [add, subtract, multiply, divide]
    
    current_operations.append(operation)
    
    """
    


def get_operations(calc):
    return calc['operations'].keys()
    """
    Returns the list of operation names supported by given calculator.
    """
    


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
    calc["history"]=[]
    
def repeat_last_operation(calc):
    if (calc['history']) ==[]:
        return None
    else:
        return calc['history'][-1][3]
