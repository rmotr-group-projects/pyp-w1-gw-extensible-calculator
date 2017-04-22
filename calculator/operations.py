
def add(*args):
    if len(args) is 1:
        return args[0]
    else:
        return sum(args)

def subtract(*args):
    first_num = args[0]
    if len(args) is 1:
        return first_num
    else:
        subtraction_list = list(args[1::])
        return first_num - sum(subtraction_list)
       

def multiply(*args):
    result = args[0]
    if len(args) is 1:
        return result
    else: 
        multiplication_list = list(args[1::])
        for num in multiplication_list:
            result *= num
        return result

def divide(*args):
    result = args[0]
    if len(args) is 1:
        return result
    else: 
        division_list = list(args[1::])
        for num in division_list:
            result /= float(num)
        return result

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
