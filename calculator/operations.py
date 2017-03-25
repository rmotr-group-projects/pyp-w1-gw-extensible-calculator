import functools
import operator
from datetime import datetime

def add(*args):
    return sum(args)
        
subtract = lambda *args: args[0] - sum(args[1:])
    
def multiply(*args):
    #product = 1
    #for i in args[0]:
        #product *= i
    product = functools.reduce(lambda x, y: x*y, args)
    return product
    

def divide(*args):
    quotient = functools.reduce(lambda x,y: float(x)/y, args)
    quotient = round(quotient, 1)
    if str(quotient)[2] == 0:
        quotient = int(str(quotient[0]))
    return quotient
    

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

def create_new_calculator(operations={}):
    
    if operations:
        new_calc = {'operations': {k : v for k, v in operations.items()}, 'history': []}
    else:
        new_calc = {'operations': {}, 'history': []}

# add your custom operations here


