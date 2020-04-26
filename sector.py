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