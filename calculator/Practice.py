def multiplication(a,b):
    result = a*b
    print(result)

n = float(input('give me a value:'))
e = float(input('give me another value:'))
choice = input('choose a function(m):')
if choice == 'm':
    multiplication(n,e)