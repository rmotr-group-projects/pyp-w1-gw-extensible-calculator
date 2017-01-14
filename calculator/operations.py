from __future__ import division


def add(*args):
    return sum(args)


def subtract(*args):
    result = args[0]

    for n in args[1:]:
        result -= n

    return result


def multiply(*args):
    result = 1

    for n in args:
        result *= n

    return result


def divide(*args):
    result = args[0]

    for n in args[1:]:
        result /= n

    return result


def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION!
    # See README for info.
    pass

# add your custom operations here
