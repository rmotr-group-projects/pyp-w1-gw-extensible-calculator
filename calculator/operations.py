
def add(*args):
    # your implementation here
    total = args[0]
    for i in args[1:]:
        total += i
    return total

def subtract(*args):
    # your implementation here
    total = args[0]
    for i in args[1:]:
        total -= i
    return total

def multiply(*args):
    # your implementation here
    total = args[0]
    for i in args[1:]:
        total *= i
    return total

def divide(*args):
    # your implementation here
    total = args[0]
    for i in args[1:]:
        total /= float(i)
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
