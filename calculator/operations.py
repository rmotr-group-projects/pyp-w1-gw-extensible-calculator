def add(*args):
    return reduce(lambda x, y: x + y, args)    

def subtract(*args):
    return reduce(lambda x, y: x - y, args)
   
def multiply(*args):
    return reduce(lambda x, y: x * y, args)

def divide(*args):
    if reduce(lambda x, y: x % y, args) == 0:
        return reduce(lambda x, y: x / y, args)
    else:
        return(reduce(lambda x, y: x / float(y), args))
   
# add your custom operations here