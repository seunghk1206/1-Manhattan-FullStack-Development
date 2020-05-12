a = float(input('give me a number:'))

if a < 10:
    print("small")
elif a >= 10:
    pass
#
#

a = float(input('give me a number:'))

if a < 10:
    print("small")
else:
    print("big")

#
#

a = float(input('give me a number:'))
b = float(input('give me a number:'))
if a < b:
    print("<")
elif a > b:
    print(">")
elif a == b:
    print("=")

#
#

a = float(input('give me a number:'))
b = float(input('give me a number:'))
if a < b:
    print(b - a)
elif a > b:
    print(a - b)
elif a == b:
    print("0")

#
#

a = int(input('give me a number:'))

if a%2 == 0:
    print("even")
elif a%2 == 1:
    print('odd')

#
#

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for eachNumber in listA:
    for eachNum in listA:
        print(eachNumber * eachNum)