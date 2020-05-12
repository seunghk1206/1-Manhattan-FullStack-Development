import math
def absolute(a):#definition of the function, absolute
    result = abs(a)
    print(result)

n = float(input('give me value of n: '))# n is the input what the user puts
choice = input('choice (q)')
if choice == 'q': #first step to a calculator. If the user presses q in his/her computer, the computer will print the value of the function
    print(absolute(n))