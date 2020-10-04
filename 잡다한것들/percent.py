def Slalash(var):
    print(var)
    b = str(eval(var))
    if '.' in b:
        a = list(b.split('.'))
        return a[0]
    else:
        return b
print(str(input()))
print(Slalash(str(50/23)))
print(50//23)
def percent(var):
    return int(var.split('/')[0]) - (int(Slalash(var)) * int(var.split('/')[1]))
print(percent(str(input())))