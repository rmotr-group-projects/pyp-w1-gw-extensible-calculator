
def add(*args):
    # your implementation here
    add = sum(args)
    return add

def subtract(*args):
    # your implementation here
    return args[0] - sum(args[1:])
    

def multiply(*args):
    # your implementation here
    product = 1
    for i in args:
        product *= i
    return product

def divide(*args):
    # your implementation here
    total = float(args[0])
    for i in args [1:]:
        total /= float(i)
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
