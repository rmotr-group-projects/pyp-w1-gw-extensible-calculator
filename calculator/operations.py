from functools import reduce


def add(*args):
    return sum(args)


def subtract(*args):
    return reduce(lambda x, y: x - y, args)


def multiply(*args):
    return reduce(lambda x, y: x * y, args)


def divide(*args):
    return reduce(lambda x, y: float(x) / float(y), args)



# add your custom operations here
def exponent(*args):
    '''Returns the first arg raised to the exponent of the 2nd arg, raised to the 3rd arg, etc..)'''
    if len(args) < 2:
        return args
    else:
        count = 0
        for arg in args:
            if count == 0:
                value = arg
            else:
                value = value ** arg
            count += 1
    return value