

##

howMany = int(input("how many cards? "))
limit = int(input("what would you set as a limit? "))
absVal = []
EL = []
values = []
negativeValues = []
sum = 0
if 3 <= howMany <= 100:
    Cnumbers = list(input().split(', '))
    if len(Cnumbers) == howMany:
        for each in Cnumbers:
            EL.append(int(each) - int(limit))
        sorted(EL)
        for eachNum in EL:
            if eachNum < 0:
                negativeValues.append(eachNum)
            print(negativeValues)
        for each in EL:
            absVal.append(abs(each))
            print(absVal)
        for each in absVal:
            Index = int(absVal.index(min(absVal)))
            IndexX = int(negativeValues.index(max(negativeValues)))
            if Index > IndexX:
                values.append(min(absVal)+limit)
            elif Index <= IndexX:
                values.append(-min(absVal)+limit)
            absVal.remove(min(absVal))
        for a in range(len(values)):
            sum += int(values[a])
        print(sum)
    else:
        print("only", howMany, "cards accepted")
else:
    print("too many cards, error")
