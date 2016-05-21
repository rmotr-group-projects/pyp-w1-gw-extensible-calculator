
def add(*args):
    return sum(args)
    

def subtract(*args):
    return args[0] - sum(args[1:])
    

def multiply(*args):
    value = 1
    for a in args:
        value *= a
    return value
    

def divide(*args):
    value = float(args[0])
    for a in args[1:]:
        value /= a
    return value


# add your custom operations here
def square(arg):
    return arg**2