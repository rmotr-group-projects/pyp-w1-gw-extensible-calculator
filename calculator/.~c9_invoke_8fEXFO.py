from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations={}):
    dictionary = {
            'operations': operations,
            'history': []
        }
        
    return dictionary

def perform_operation(calc, operation, params):
    """
    
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
                   
    def test_perform_operation(self):
        res = perform_operation(self.calc, 'add', (5, 3))
        self.assertEqual(res, 8)
    """
    def add_to_history(op_result):
        calc['history'].append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), operation, params, op_result))
        date.strftime('%Y-%m-%d %H:%M:%S')
    try: 
        result = calc['operations'].get(operation)(*params)
    except Exception:
        raise InvalidParams()
        
    
    add_to_history(result)
    
        
    return result


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
                       add_new_operation(self.calc, operation={'add': self.add})
    """
    if type(operation) == dict and callable(list(operation.values())[0]):
        calc['operations'].update(operation)
    else:
        raise InvalidOperation("Given operation is invalid.")


def get_operations(calc):
    return list(calc['operations'].keys())
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
    calc['history'] = []

def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if len(calc['history']) == 0:
        return None 

    return calc['history'][-1][-1]

