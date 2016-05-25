from functools import reduce
import sympy

def add(*args):
    # your implementation here
    return sum(args)

def subtract(*args):
    # your implementation here
    return reduce(lambda x,y: x-y, args)

def multiply(*args):
    # your implementation here
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    # your implementation here
    return reduce(lambda x,y: float(x)/float(y), args)

# add your custom operations here
def plot(*args):
    expression = sympy.symbols(args[0]) #Turn the 1st argument from text to math xpression
    sympy.plotting.textplot(expression, args[1], args[2]) #Plot the expression