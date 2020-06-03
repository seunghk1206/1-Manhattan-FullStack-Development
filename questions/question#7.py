a1 = []
n1 = []
a = int(input())
for each in range(a):
    x, y = map(str, input().split(' '))
    a1.append(x)
    n1.append(y)
for i in range(len(a1)):
    print(min(a1), ' ', n1[a1.index(min(a1))])
    n1.remove(n1[a1.index(min(a1))])
    a1.remove(min(a1))