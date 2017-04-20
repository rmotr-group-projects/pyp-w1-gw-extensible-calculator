from functools import reduce
import operator


def add(*args):
    return sum(args)

def subtract(*args):
    if args:
        answ = args[0]
        for item in args[1:]:
            answ = answ-item
        return answ
    else:
        raise ArithmeticError

def multiply(*args):
    mult = reduce(operator.mul, args, 1)
    return mult

def divide(*args):
    if args:
        answ = float(args[0])
        for item in args[1:]:
            answ = answ/float(item)
        return answ
    else:
        raise ArithmeticError

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here

#PYTHONPATH=. py.test tests/test_main.py