#python built-in function -> print(), input(), float() 
#all of them are function abs(), import math
#library 

#HWOne.py
#HW 1 -> Make a function that user can change the integer into abs value.
#Please give me an integer:
#-15
#The absolute value of -15 : 15

#HWTwo.py
# HW 2 -> Make several functions to build a calculator.

def order(): # Name of Function
    print('Give me a name of a drink') #prompt a message to user
    drink = input() #store the data to drink variable
    print(drink, 'is what you want')

order()

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

addition(3,4) #함수호출
multiplication(4,5)
subtraction(5,6)
division(7,8)