
def add(*args):
    return sum(args)
    

def subtract(*args):
    # your implementation here
    # subtract(10, 2, 1) = 10 - 2 - 1
    # subtract(10)
    value = args[0]
    for item in args[1:]:
        value -= item
        
    return value

def multiply(*args):
    value = args[0]
    for item in args[1:]:
        value *= item
        
    return value

def divide(*args):
    value = float(args[0])
    for item in args[1:]:
        value /= item
        
    return value

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here