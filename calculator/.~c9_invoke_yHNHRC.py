from __future__ import division

def add(*args):
    
            print(args[0])
            return args[0]
        print (sum(args))
        return sum(args)

def subtract(*args):
        if len(args) == 1:
            print(args[0])
        print (args[0] - sum(args[1::]))
        return args[0] - sum(args[1::])
    
def multiply(*args):
    multiplication = 1
    for item in args:
        multiplication = multiplication * item
        print (multiplication)
    return multiplication
        
def divide(*args):
    if len(args)==1:
        return args[0]
    division=args[0]    
    for item in args[1::]:
        division=division/item
    print (division)
    return division

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

'''   
try:
except InvalidOperation:
    raise InvalidOperation('Given operation is invalid.')
except InvalidParams:
    raise InvalidParams('Given params are invalid.')
'''
