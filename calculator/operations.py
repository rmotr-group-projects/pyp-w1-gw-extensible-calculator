
def add(*args):
    return sum(args)
    
def subtract(*args):
    if len(args) <= 1:
        return args[0]
    result = args[0]
    for x in range(1,len(args)):
        result -= args[x]
    return result

def multiply(*args):
    if len(args) <= 1:
        return args[0]
    result = args[0]
    for x in range(1,len(args)):
        result *= args[x]
    return result
    

def divide(*args):
    if len(args) <= 1:
        return args[0]
    result = float(args[0])
    for x in range(1,len(args)):
        result /= args[x]
    return result


def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
