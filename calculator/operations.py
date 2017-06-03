
def add(*args):
    return reduce((lambda x, y: x+y), args)

def subtract(*args):
    return reduce((lambda x, y: x-y), args)

def multiply(*args):
    return reduce((lambda x, y: x*y), args)


def divide(*args):
    return reduce((lambda x, y: float(x)/float(y)), args)


def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

