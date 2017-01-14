import operator
from functools import reduce 
#from sympy import symbols, cos
#from sympy.plotting import plot



def add(*args):
    return sum(args)

def subtract(*args):
    answer = args[0]
    for item in args[1:]:
        answer = answer - item
    return answer

def multiply(*args):
    answer = reduce(operator.mul, (args), 1)
    return answer

def divide(*args):
    answer = float(args[0])
    for item in args[1:]:
        answer = answer / float(item)
    return answer

def plot(*args):
    pass
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    #sympy library
    # args[0] = '-x**2' OR 'x*x'
    
    # plotvars = re.findall('[A-z]')
    # #/^[A-z]+$/
    # firstarg=arg[0]
    # for i in firstarg:
    
    # x = symbol('the ltter in args[0]')
    
    # plot(args[0], xlim=(args[1],args[2]))
    
    #plot(sympy.symbols('x')**2, xlim=(-2,2))