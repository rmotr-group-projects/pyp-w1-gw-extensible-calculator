from functools import reduce
from operations import *
def addition(*args):
    result = reduce(lambda acc, y: acc + y, args, 0)
    return result
    
print(addition(1))

def multiplication(*args):
    
    result = reduce(lambda acc, y: acc * y, args, 1)
    return result
print(multiplication(4, 2, 3))




def division(*args):
    result = reduce(lambda acc, y: acc / y, args[1:], args[0])
    return result
    
print division(100,5,4)




def subtract(*args):
    # your implementation here
    result = reduce(lambda acc, y: acc - y, args[1:], args[0])
    return result
print(subtract(10,1,50), " =subtraction")


def create_new_calculator(operations={'add':add,'subtract':subtract,'multiply':multiply,'divide':divide}):
    myops={}
    for key in operations:
        myops[key] = operations[key]
    return myops
    
print(create_new_calculator())