import math
def absolute(a):#definition of the function, absolute
    result = abs(a)
    print(result)

def multiplication(a, b): # Mult a, b are parameters
    """DocString
    This is multiplication"""
    result = a * b
    print(result)

def addition(a, b):#define
    result = a + b
    print(result)

def subtraction(a, b):
    result = a - b
    print(result)

def division(a, b):
    result = a / b
    print(result)

n = float(input('give me value of n: '))# n is the input what the user puts
choice = input('choice (abs, mult, add, subt, div)')
if choice == 'abs': #first step to a calculator. If the user presses q in his/her computer, the computer will print the value of the function
    print(absolute(n))
elif choice == 'mult':
    n1 = float(input('give me value of n1: '))
    print(multiplication(n,n1))
elif choice == 'add':
    n1 = float(input('give me value of n1: '))
    print(addition(n,n1))
elif choice == 'subt':
    n1 = float(input('give me value of n1: '))
    print(subtraction(n,n1))
elif choice == 'div':
    n1 = float(input('give me value of n1: '))
    print(division(n,n1))