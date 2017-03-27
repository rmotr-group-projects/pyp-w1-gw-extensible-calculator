
def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

def divide(*args):
    result = args[0]
    for i in args[1:]:
        result = float(result) / i
    return result

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
