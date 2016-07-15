from __future__ import division

from collections import defaultdict

def add(*args):
    add_numbers = lambda a, b : a+b
    current_sum = 0
    if len(args) > 0 :
        for item in args :
            #print "ITEM IS : ", item
            current_sum = add_numbers(current_sum, item)
        return current_sum
    else :
        return AttributeError
    
def subtract(*args):
    subtract_numbers = lambda a, b : a-b
    if len(args) > 0 :
        current_diff = args[0]
        for item in args[1:] :
            current_diff = subtract_numbers(current_diff, item)
        return current_diff
    else :
        return AttributeError

def multiply(*args):
    multiply_numbers = lambda a, b : a*b
    current_product = 1
    if len(args) > 0 :
        for item in args :
            current_product = multiply_numbers(current_product, item)
        return current_product
    else :
        return AttributeError
    

def divide(*args):
    divide_numbers = lambda a, b : a/b
    if len(args) > 0 :
        current_quotient = args[0]
        for item in args[1:] :
            current_quotient = divide_numbers(current_quotient, item)
        return current_quotient
    else :
        return AttributeError
    
# add your custom operations here