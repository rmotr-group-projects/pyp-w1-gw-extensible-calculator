from functools import reduce

def add(*args):
    # your implementation here
    return sum(args)

def subtract(*args):
    # your implementation here
    return args[0] - sum(args[1::])

def multiply(*args):
    # your implementation here
    answer = 1
    for nums in args:
        answer *= nums
    return answer

def divide(*args):
    # your implementation here
    return reduce(lambda x, y: float(x) / y, args[1:], args[0])

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
