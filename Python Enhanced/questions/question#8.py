a = int(input())
LoP = []
LoP2 = []
g = 0
for i in range(a):
    x = input()
    LoP.append(x)
for each in range(a):
    for n in LoP[each]:
        if g >= 0:
            if n == '(':
                g += 1
            elif n == ')':
                g -= 1
        elif g < 0:
            print('NO')
            break
    if g == 0:
        print('YES')
    elif g > 0:
        print('NO')
    g = 0
#python ./questions/question#8.py
'''
))((()))
()(())
'''