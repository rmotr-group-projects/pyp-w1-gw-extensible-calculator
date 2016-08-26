
def add(*args):
    x = float(sum(args))
    return x

def subtract(*args):
    # your implementation here
    x = float(args[0])
    for arg in args[1:]:
        x = x-float(arg)
    return x
    
def multiply(*args):
    # your implementation here
    x = float(args[0])
    for arg in args[1:]:
        x = x*float(arg)
    return x

def divide(*args):
    # your implementation here
    x = float(args[0])
    for arg in args[1:]:
        x = x/float(arg)
    return x
    
def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
