
def add(*args):
    return sum(args)
    
def subtract(*args):
    return args[0] - sum(args[1:])


def multiply(*args):
    total = args[0]
    for arg in args[1:]:
        total *= arg
    return total

# args = [1,2,34,4,5]
#return reduce(lambda x, y: float(x) / y, args)
def divide(*args):
    total = float(args[0])
    for arg in args[1:]:
        total /= float(arg)
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
