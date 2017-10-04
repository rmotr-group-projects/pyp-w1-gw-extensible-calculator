
def add(*args):
    # your implementation here
    return sum([arg for arg in args])

def subtract(arg, *args):
    # your implementation here
    # count = arg
    # for num in args:
    #     count -= num
    # return count
    return arg - sum([arg for arg in args])

def multiply(arg, *args):
    # your implementation here
    count = arg
    for num in args:
        count *= num
    return count

def divide(arg, *args):
    # your implementation here
    count = float(arg)
    for num in args:
        count /= num
    return count

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
