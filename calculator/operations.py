
def add(*args):
    # your implementation here
    return sum(args)
        
def subtract(*args):
    # your implementation here
    res = args[0]
    for num in args[1:]:
        res -= num
    
    return res

def multiply(*args):
    # your implementation here
    res = args[0]
    for num in args[1:]:
        res *= num
    
    return res

def divide(*args):
    # your implementation here
    res = args[0]
    for num in args[1:]:
        res /= float(num)
    
    return res

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
