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