from operator import add,sub,mul 

def add(*args):
    # your implementation here
    return reduce((lambda x, y: x + y), args)

def subtract(*args):
    # your implementation here
    #return map((lambda x, y: x - y), args)
    return reduce(sub,args)
    
    
def multiply(*args):
    # your implementation here
    return reduce((lambda x, y: x * y), args)

def divide(*args):
    # your implementation here
    #check to see if second or further arg is 0
    return reduce((lambda x, y: float(x) / y), args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
