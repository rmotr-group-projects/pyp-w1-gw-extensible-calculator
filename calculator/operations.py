
def add(*args):
    return sum([arg for arg in args])

def subtract(arg, *args):
    count = arg
    for num in args:
        count -= num
    return count

def multiply(arg, *args):
    count = arg
    for num in args:
        count *= num
    return count

def divide(arg, *args):
    count = float(arg)
    for num in args:
        count /= num
    return count

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
