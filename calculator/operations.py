
def add(*args):
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum

def subtract(*args):
    difference = args[0]
    for arg in args[1:]:
        difference -= arg
    return difference

def multiply(*args):
    product = args[0]
    for arg in args[1:]:
        product *= arg
    return product

def divide(*args):
    quotient = args[0]
    for arg in args[1:]:
        quotient /= float(arg)
    return quotient

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here