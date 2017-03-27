
def add(*args):
    output = 0
    count = 0
    for arg in args:
        if count == 0:
            output = arg
        else:
            output += arg
        count += 1
    return output

def subtract(*args):
    output = 0
    count = 0
    for arg in args:
        if count == 0:
            output = arg
        else: 
            output = output - arg
        count += 1
    return output

def multiply(*args):
    output=1
    for arg in args:
        output*=arg
    return output

def divide(*args):
    count = 0
    output = 0.0
    for arg in args:
        if count == 0:
            output = arg * 1.0
        else:
            output = output / arg
        count += 1
    return output

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here



