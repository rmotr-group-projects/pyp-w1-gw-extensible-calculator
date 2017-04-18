from functools import reduce

# def add(*args):
#     return reduce(lambda *args: sum(*args)
    

# def subtract(*args):
#     sum = args[0]
#     for arg in args[1:]:
#         sum -= float(arg)
#     return sum

# def multiply(*args):
#     # sum = args[0]
#     # for arg in args[1:]:
#     #    sum = float(sum)*arg
#     # return sum
#     return reduce(lambda x, y: x*y, arg)

# def divide(*args):
#     sum = args[0]
#     for arg in args[1:]:
#         sum = float(sum)/arg
#     return sum


def add(*args):
    return reduce(lambda x, y: x + y, args)

def subtract(*args):
    return reduce(lambda x, y: x - y, args)

def multiply(*args):
    return reduce(lambda x, y: x * y, args)

def divide(*args):
    return reduce(lambda x, y: float(x) / float(y), args)


def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
