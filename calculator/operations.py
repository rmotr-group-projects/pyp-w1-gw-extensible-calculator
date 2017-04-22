def add(*args):
    return(sum(args))

def subtract(*args):
    ans = float(args[0])
    if len(args) > 1:
        for each in args[1:]:
            ans -= each
            print(ans)
        return ans
    else:
        ans = args[0]
        return ans

def multiply(*args):
    ans = float(args[0])
    for each in args[1:]:
        ans *= each
    return ans

def divide(*args):
    ans = float(args[0])
    for each in args[1:]:
        ans /= each
    return ans
