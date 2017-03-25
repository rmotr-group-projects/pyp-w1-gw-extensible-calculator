
def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])
    
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def divide(*args):
    total = args[0]
    for i, arg in enumerate(args):
        if i == 0:
            continue
        total /= float(arg)
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
