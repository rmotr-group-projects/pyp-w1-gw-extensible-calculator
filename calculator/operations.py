
def add(*args):
    # your implementation here
    return operate(lambda x, y : x + y, *args)

def subtract(*args):
    # your implementation here
    return operate(lambda x, y: x - y, *args)

def multiply(*args):
    # your implementation here
    return operate(lambda x, y : x * y, *args)

def divide(*args):
    # your implementation here
    return operate(lambda x, y : float(x) / y, *args)

# add your custom operations here
def operate(operation, *args):
    if not args:
        return 0
    
    output = args[0]
    for number in args[1:]:
        output = operation(output, number)
    return output