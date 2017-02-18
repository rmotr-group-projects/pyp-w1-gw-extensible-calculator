
#def add(*args):
add = lambda first, *args: first + sum(args)

#def subtract(*args):
subtract = lambda first, *args: first - sum(args)

def multiply(first, *args):
	total = first
	for num in args:
		total *= num
	return total

def divide(first, *args):
    div = float(first)
    for num in args:
        div /= num
    return div

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
#PYTHONPATH=. py.test -s tests -k