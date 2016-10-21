from sympy import plot as symplot
from functools import reduce

def add(*args):
    # Returns the sum of numbers
    return sum(args)

def subtract(*args):
    # Returns the subtraction of numbers
    return args[0] - sum(args[1:])

def multiply(*args):
    # Returns the multiplication of numbers
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    #  Returns the division of numbers
    total = float(args[0])
    print (total)
    for i in args[1:]:
        total = total / i
        print(total, i)
    return total

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    my_plot = symplot(args[0], ('x', args[1], args[2]))
    print(my_plot)
    return my_plot

# add your custom operations here

plot('-x**2', -2, 2)