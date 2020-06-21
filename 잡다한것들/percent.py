def percent(var):
    b = str(var)
    if '.' in b:
        a = list(b.split('.'))
        return a[0]
    else:
        return b

print(percent(50/23))
print(50//23)