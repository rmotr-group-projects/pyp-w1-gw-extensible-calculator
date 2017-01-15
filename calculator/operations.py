import functools


def add(*args):
    return sum(args)

def subtract(*args):
    return functools.reduce(lambda x, y: x-y, args)

def multiply(*args):
    return functools.reduce(lambda x, y: x*y, args)


def divide(*args):
    return float(functools.reduce(lambda x, y: x/float(y), args))


def plot(*args):
    pass