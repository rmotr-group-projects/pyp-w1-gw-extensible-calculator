from datetime import datetime

from calculator.operations import add, multiply, subtract, divide, exponent
from calculator.exceptions import InvalidParams, InvalidOperation

def create_new_calculator(operations={}):
    
    new_calc = {
        'operations' : {},
        'history' : []
    }
    
    new_calc['operations'] = operations 
    return new_calc

def perform_operation(calc, operation, params):#
    for num in params:
        if not isinstance(num, (int)) and not isinstance(num, (float)):
            raise InvalidParams('Given params are invalid.')

    for operators in calc['operations'].keys():
        if operation == operators:
            break
    else:
        raise InvalidOperation('Given operation is invalid.')


    time_of_exec = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = calc["operations"][operation](*params)
    history_record = (time_of_exec, operation, params, result)
    calc["history"].append(history_record)
    
    return result


def add_new_operation(calc, operation):
    if not isinstance(operation, (dict)):
        raise InvalidOperation('Given operation is invalid.')
    else:
        operation_name = ''.join([operation_name for operation_name in operation.keys()])
        calc['operations'][operation_name] = operation[operation_name]


def get_operations(calc):
    return [operation for operation in calc['operations'].keys()]


def get_history(calc):
    return calc['history']


def reset_history(calc):
    calc['history'] = []


def repeat_last_operation(calc):
    if calc['history'] == []:
        return None
    else:
        last_action = calc['history'][-1]
        return last_action[3]

