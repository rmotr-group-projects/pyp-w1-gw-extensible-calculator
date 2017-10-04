add = lambda *args : sum(args)

def subtract(*args):
    s_base = args[0]
    s_rest = args[1:]
    
    for num in s_rest:
        s_base -= num
    
    return s_base

def multiply(*args):
    p_base = 1
    
    for num in args:
        p_base *= num
    
    return p_base

def divide(*args):
    d_base = float(args[0])
    d_rest = args[1:]
    
    for num in d_rest:
       d_base /= num
    
    return int(d_base) if int(d_base) == d_base else d_base

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
