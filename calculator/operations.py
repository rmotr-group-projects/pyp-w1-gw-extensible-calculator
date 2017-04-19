try:
    from functools import reduce
except ImportError:
    # Py2
    pass


def add(*args):
    # your implementation here
    return sum(args)

def subtract(*args):
    # your implementation here
    return args[0] - sum(args[1:])

def multiply(*args):
    # your implementation here
    return reduce(lambda x, y: x * y, args, 1)

def divide(*args):
    # your implementation here
    return reduce(lambda x, y: float(x) / y, args[1:], args[0])
