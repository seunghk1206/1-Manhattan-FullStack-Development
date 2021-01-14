
addition = lambda a : a+5
print(addition(5))

def funcReturn(n):
    return lambda a : a*n

fun = funcReturn(5)
print(fun(5))