def add(*args):
    return sum(args[:])   

def subtract(*args):
    return args[0] - sum(args[1:])
   
def multiply(*args):
    value = args[0]
    for item in args[1:]:
        value *= item
    return value
    

def divide(*args):
    int_value = args[0]
    float_value = args[0]
    for item in args[1:]:
        int_value /= item
        float_value /= item
    if int_value != float_value:
        return float_value
    return int_value
        
    #if reduce(lambda x, y: x % y, args) == 0:
      #  return reduce(lambda x, y: x / y, args)
    #else:
     #   return(reduce(lambda x, y: x / float(y), args))
   
# add your custom operations here