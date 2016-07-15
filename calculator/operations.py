
def add(*args):
    return sum(args)

def subtract(*args):
	return args[0]-(sum(args[1:]))

def multiply(*args):
    if len(args)==1:
        return args[0]
    elif len(args) >= 2:
        m = args[0]
        for x in args[1:]:
            m = m*x
        return m
    else:
        return None
    pass

def divide(*args):
    if len(args)==1:
        return args[0]
    elif len(args) >= 2:
        return float(args[0])/multiply(*args[1:])