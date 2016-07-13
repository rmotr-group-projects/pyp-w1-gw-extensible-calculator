from functools import reduce
def add(*args):
    # your implementation here
    return reduce(lambda x,y: x+y, args)

def subtract(*args):
    # your implementation here
    return reduce(lambda x,y: x-y, args)

def multiply(*args):
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    # your implementation here
    return reduce(lambda x,y: x/y, args)

# add your custom operations here
