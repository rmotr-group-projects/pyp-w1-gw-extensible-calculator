import operator
from functools import reduce 
from sympy import symbols
from sympy.plotting import plot as pl
import re



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
    eqn = args[0]
    sym = ""
    pattern = re.compile("[A-z]")
    for i in eqn:
        if pattern.match(i):
            sym = i
    
    return pl(eqn, (sym, args[0], args[1]))
    