
def add(*args):
    result=args[0]
    if len(args)>1:
        for n in args[1:]:
            result+=n
    return result

def subtract(*args):
    result=args[0]
    if len(args)>1:
        for n in args[1:]:
            result-=n
    return result

def multiply(*args):
    result=args[0]
    if len(args)>1:
        for n in args[1:]:
            result*=n
    return result

def divide(*args):
    result=float(args[0])
    if len(args)>1:
        for n in args[1:]:
            result/=float(n)
    return result
    
def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
