def factorial(x):
    if x == 0:
        return 1
    else: 
        return x * factorial(x-1)

def f(x, n):
    return (((-1)**n)*x**(2*n+1)/factorial(2*n+1))

def sin(x, n):
    x = x%360
    if x%90 == 0:
        if (x//90)%2 == 1:
            if ((x//90)//2)%2 == 1:
                return -1
            else: 
                return 1
        else:
            return 0
    else:
        pi2deg = 3.1415/180
        if n == 0:
            return f(x*pi2deg, n)
        else:
            return f(x*pi2deg, n) + sin(x,n-1)

def g(x, n):
    return (((-1)**n)*x**(2*n)/factorial(2*n))

def cos(x, n):
    x = x%360
    if x%90 == 0:
        if (x//90)%2 == 1:
            return 0
        else:
            if x%360 == 0:
                return 1
            else:
                return -1
    else:
        pi2deg = 3.1415/180
        if n == 0:
            return g(x*pi2deg, n)
        else:
            return g(x*pi2deg, n) + cos(x,n-1)

def tan(x, n):
    return sin(x, n)/cos(x, n)#maximum limit n = 84

def compoundAddCos(a, b):
    return cos(a, 84)*cos(b, 84) - sin(a, 84)*sin(b, 84)
def MultipleSin(x, limit):
    return 2**(limit-1)*sin(x, 84)*MultipleSinBody(x, 1, limit)
def MultipleSinBody(x, n, limit):
    if n + 1 != limit-1:
        return sin(n*180/limit+x, 84)*MultipleSinBody(x, n+1, limit)
    else:
        return sin(n*180/limit+x, 84)
def eulerNumber(precision):
    if precision != 0:
        return 1/factorial(precision)+eulerNumber(precision-1)#20 is the limit threshold. It makes no difference in limit is larger than 20
    else:
        return 1

def eulerNumber2(precision):
    return (1+precision)**(1/precision)#precision -> 0, more precise the e is

def eulerNumber3(precision):
    return (1+1/precision)**(precision)#precision -> inf, more precise the e is

print(MultipleSin(1, 30))
print(eulerNumber3(1/0.000001))