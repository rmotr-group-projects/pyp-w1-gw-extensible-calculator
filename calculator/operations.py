from .exceptions import InvalidParams

def add(*args):
    g = lambda *arg: sum(arg)
    return g(*args)
#still doesnt work for tuple test

def subtract(*args):
    g = lambda *arg: sum(arg)
    print(args[0])
    return args[0]-g(*args[1:])
    
    #var = [arg for arg in args]
    #try:
    #    return var[0]-sum(var[1:])
    #except:
    #    raise InvalidParams("Given params are invalid.")
        
def multiply(*args):
    # your implementation here
    #var = [arg for arg in args]
    #return var[-1] * multiply(var[0:-1])
    product = 1
    for i in args: #going to come back and make more pythonic
        product *= i
    return product

def divide(*args):
    # your implementation here
    var = [arg for arg in args]
    ans = var[0]
    for arg in var[1:]:
        if arg == 0:
            raise InvalidParams("Given params are invalid.")
        ans = ans / arg
    
    return ans
    


# add your custom operations here
