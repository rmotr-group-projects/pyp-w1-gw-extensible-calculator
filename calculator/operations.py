def add(*args):
    return sum(args)

def subtract(*args):
    total = args[0]
    for number in args[1:]:
       total -= number
       
    return total

def multiply(*args):
    total = 1
    for number in args:
        total *= number
    
    return total

def divide(*args):
    total = float(args[0])
    for number in args[1:]:
       total /= number
       
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass