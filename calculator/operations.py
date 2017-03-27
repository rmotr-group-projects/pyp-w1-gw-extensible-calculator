
def add(*args):
    '''
    Returns sum of all arguments
    '''
    return sum(args)

def subtract(*args):
    count = args[0]
    i = 1
    while i < len(args):
        count -= args[i]
        i += 1
    return count

def multiply(*args):
    # your implementation here
    count = 1
    i = 0
    for argument in args:
        count *= args[i]
        i += 1
    return count
        

def divide(*args):
    count = float(args[0])
    i = 1
    while i < len(args):
        count /= args[i]
        i += 1
    return  count
        

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
