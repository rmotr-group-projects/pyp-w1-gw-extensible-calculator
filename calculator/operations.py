from .exceptions import InvalidParams


def add(*args):
    return sum(args)


def subtract(*args):
    if args[0]:
       return args[0] - sum(args[1:])
    else:
        return None
        
        
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
    

def divide(*args):
    var = [arg for arg in args]
    ans = var[0]
    for arg in var[1:]:
        if arg == 0:
            raise InvalidParams("Given params are invalid.")
        ans = ans / arg
    return ans
    


