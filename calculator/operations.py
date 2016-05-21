from .exceptions import InvalidParams
import sympy

def add(*args):
    # your implementation here
    return sum(args)

def subtract(*args):
    # your implementation here
    result = args[0]
    for i in args[1:]:
        result -= i
    return result

def multiply(*args):
    # your implementation here
    result = args[0]
    for i in args[1:]:
        result *= i
    return result

def divide(*args):
    # your implementation here
    result = args[0]
    for arg in args[1:]:
        result /= float(arg)  # float division for python 2
    return result

# add your custom operations here
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
    
"""
x = sympy.symbols('x')
print sympy.textplot(-x**2,-2,2)

print sympy.textplot(-x**2,-2,False) #Plotted -2:0
print sympy.textplot(-x**2,-2,True) #Plotted -2:1
print sympy.textplot(-x**2,-2,'2') #Plotted -2:2
print sympy.textplot(-x**2,-2,'a') #Raised ValueError: could not convert string to float: a
print sympy.textplot(-x**2,-2,-5) #Plotted on a reversed axis
print sympy.textplot(-x**2,-2) #Raised TypeError: textplot() takes at least 3 arguments
"""

'''validation steps:
1. exactly 3 params
2. first param is a valid function of x
3. second and third params are numbers
print sympy.textplot(-x**2,-2,False)
print sympy.textplot(-x**2,-2,'2')

4. third param is greater than second param
'''