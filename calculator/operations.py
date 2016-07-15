
def add(*args):
    return sum(args)

def subtract(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] - sum(args[1:])

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = float(args[0])
    for num in args[1:]:
        result /= num
    return result
#   return (args[0]) / multiply(args[1:])
# add your custom operations here
