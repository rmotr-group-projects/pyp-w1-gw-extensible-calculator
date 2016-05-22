from __future__ import division
from functools import *
def add(*args):
    #print("my args is {}".format(args))
    result = reduce(lambda acc, y: acc + y, args, 0)
    return result

def subtract(*args):
    # your implementation here
    result = reduce(lambda acc, y: acc - y, args[1:], args[0])
    return result
    
def multiply(*args):
    result = reduce(lambda acc, y: acc * y, args, 1)
    return result

def divide(*args):
     result = reduce(lambda acc, y: acc / y, args[1:], args[0])
     return result

# add your custom operations here
