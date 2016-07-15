from datetime import datetime


from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations={}):
    # returns a new calculator with an optional set of operations
    return {'operations' : operations, 'history' : []}


def perform_operation(calc, operation, params):
    # performs an operation if possible
    if operation not in calc['operations']:
        raise InvalidOperation("Given operation is invalid.")
    try:
        result = calc['operations'][operation](*params)
    except:
        raise InvalidParams("Given params are invalid.")

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    calc['history'].append((now,operation,params,result))
    return result


def add_new_operation(calc, operation):
    # adds a new operation to the calculator if possible
    try:
        calc['operations'].update(operation)
    except:
        raise InvalidOperation("Given operation is invalid.")


def get_operations(calc):
    return [operation for operation in calc['operations']]
        

def get_history(calc):
    return calc['history']


def reset_history(calc):
    calc['history'] = []


def repeat_last_operation(calc):
    # returns the last calculated result if possible, otherwise returns None
    if calc['history']:
        return calc['history'][-1][-1]
    else:
        return None
    
