
def add(*args):
    return reduce(lambda acc, y: acc + y, args, 0)
    
def subtract(*args):
    return reduce(lambda acc, y: acc - y, args[1:], args[0])

def multiply(*args):
    return reduce(lambda acc, y: acc * y, args, 1)
    
def divide(*args):
    return reduce(lambda acc, y: acc / y, args[1:], float(args[0]))

def square_root(*args):
    if len(args) == 1:
        return args[0] ** 0.5
    else:
        return tuple(arg ** 0.5 for arg in args)
    
def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here