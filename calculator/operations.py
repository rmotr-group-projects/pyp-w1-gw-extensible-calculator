
def add(*args):
	ans = 0
	for arg in args:
		ans += arg
	return ans


def subtract(*args):
    ans = args[0]
    for arg in args[1:]:
        ans -= arg
    return ans
    
    
def multiply(*args):
    ans = args[0]
    for arg in args[1:]:
        ans *= arg
    return ans

def divide(*args):
    ans = args[0]
    for arg in args[1:]:
        ans /= float(arg)
    return ans

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
