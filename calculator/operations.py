from calculator.exceptions import *
import sympy

# Base operations
def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for i in args[1:]:
        result -= i
    return result

def multiply(*args):
    result = args[0]
    for i in args[1:]:
        result *= i
    return result

def divide(*args):
    result = args[0]
    for i in args[1:]:
        result /= float(i)  # float division for python 2
    return result


# Custom operations
def square_root(arg):
    return arg ** 0.5
    
def plot(function_string, xmin, xmax):
    '''
    Reads in 3 parameters:
    a function as a string: '-x**2'
    x min: -2
    x max: 2
    Calls sympy.textplot to print a text image of the function
    '''
    x = sympy.symbols('x')
    print(sympy.textplot(eval(function_string), xmin, xmax))
    