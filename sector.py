##$$%%^^
listO = []
listC = []
I = 0
for U in range(10):
    a = int(input("Number"))
    listO.append(a % 42)

for each in listO:
    for eachNum in listO:
        if each == eachNum:
            listO.remove(each)
    
for h in listO:
    I += 1

print(I * 2, "개의 숫자는 제각각")

