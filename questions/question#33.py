inp = list(map(str, input().split()))
inp2 = list(map(str, input().split()))

numInp = []
numInp2 = []
for each in inp:
    try:
        numInp.append(float(each))
    except:
        pass

for each in inp2:
    try:
        numInp2.append(float(each))
    except:
        pass

n = len(numInp)
        
summateMult = sum([numInp[i]*numInp2[i] for i in range(len(numInp))])
sumX = sum(numInp)
sumY = sum(numInp2)

numerator = n*summateMult - sumX*sumY

summateSquareX = sum([each**2 for each in numInp])
summateSquareY = sum([each**2 for each in numInp2])

denominator = (n*summateSquareX-sumX**2)**(1/2)*(n*summateSquareY-sumY**2)**(1/2)

print(numerator/denominator)