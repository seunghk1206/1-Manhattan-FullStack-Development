x = float(input("give me an x value:"))
y = float(input("give me an y value:"))

if x > 0 and y > 0:
    print("이 점은 제 1 사분면 위에 있다.")
elif x < 0 and y < 0:
    print("이 점은 제 4 사분면 위에 있다.")
elif x < 0 and y > 0:
    print("이 점은 제 2 사분면 위에 있다.")
elif x > 0 and y < 0:
    print("이 점은 제 3 사분면 위에 있다.")
else:
    print("그 어느 사분면 위에도 있지 않다.")

## 2
c = int(input("how many times would you like to do the sum up?"))

listA = []
for eachNum in range(c):
    a, b = map(int, input().split())
    listA.append(a + b)

for x in listA:
    print(x)

##XD

p = int(input("how many stars would you like?"))

for each in range(p):
    print("*" * (each + 1))


##???
p = int(input("how many stars would you like?"))

for i in range(p):
    print(" " * (p - i), "*" * (i + 1))

##

listC = []
while True:
    w, h = map(int, input().split())
    listC.append(w + h)
    if w == 0 and h == 0:
        for g in listC:
            print(g)
        break

##:D

p = int(input("how many numbers would you like to put?"))
listJ = []
for each in range(p):
    h = int(input("value?"))
    listJ.append(h)
print(max(listJ))
print(min(listJ))

##XD
LN = []
max = 0
index = 0

for each in range(9):
    a = int(input("a number please"))
    LN.append(a)

for x in LN:
    l += 1
    if x > max:
        max = x
        index = l


print("최대값은", max, index, "번째 숫자")

##$$%%^^
listO = []

I = 0
for U in range(10):
    a = int(input("Number"))
    listO.append(a % 42)

for each in listO:
    for eachNum in listO:
        if each == eachNum:
            I += 1

print("각 숫자를 42로 나누었을때", 20 - I, "개의 숫자는 나머지가 제각각")

##4212

a = list(input().split(' '))

a.remove(max(a))

print(a)

print(max(a))

##
