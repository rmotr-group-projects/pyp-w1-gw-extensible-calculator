
def add(*args):
    ret_val=args[0]
    
    for x in args[1:]:
        ret_val+=x
    
    return ret_val

def subtract(*args):
    ret_val=args[0]
    
    for x in args[1:]:
        ret_val-=x
    
    return ret_val
    
def multiply(*args):
    ret_val=args[0]
    
    for x in args[1:]:
        ret_val*=x
    
    return ret_val

def divide(*args):
    ret_val=float(args[0])
    for x in args[1:]:
        ret_val/=float(x)
   
    return ret_val

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
