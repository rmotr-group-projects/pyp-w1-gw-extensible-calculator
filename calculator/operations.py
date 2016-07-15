
def add(*args):
    ans = 0
    print("args,", args)
    for item in args:
        ans += item
    return ans

def subtract(*args):
    ans = args[0] * 2
    for item in args:
        ans-= item
    return ans

def multiply(*args):
    ans = 1
    for item in args:
        ans *= item
    return ans

def divide(*args):
    ans = args[0] * args[0] * 1.0
    for item in args:
        ans /= item
    return ans

# add your custom operations here
