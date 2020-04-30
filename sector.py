

##

howMany = int(input("how many cards? "))
limit = int(input("what would you set as a limit? "))
absVal = []
EL = []
values = []
#negativeValues = []
sum = 0
if 3 <= howMany <= 100:
    Cnumbers = list(input().split(', '))
    if len(Cnumbers) == howMany:
        Cnumbers.sort()
        for each in Cnumbers:
            EL.append(int(each) - int(limit))
        # for eachNum in EL:
        #     if eachNum < 0:
        #         negativeValues.append(eachNum)
        #     print(negativeValues)
        for each in EL:
            absVal.append(abs(each))
            print(absVal)
        for each in range(3):
            Index = int(absVal.index(min(absVal)))
            # IndexX = int(negativeValues.index(max(negativeValues)))
            print(Cnumbers[Index])
            values.append(Cnumbers[Index])
            # if IndexX == 0:
            #     if len(negativeValues) == 0:
            #         values.append(min(absVal)+limit)
            #         print(values)
            #     elif len(negativeValues) == 1:
            #         values.append(min(EL))
            #     absVal.remove(min(absVal))
            # elif IndexX > 0:
            #     if Index > IndexX:
            #         values.append(min(absVal)+limit)
            #         print(values)
            #     elif Index <= IndexX:
            #         values.append(-min(absVal)+limit)
            #         print(values)
            #         negativeValues.remove(negativeValues[IndexX])
            #         print(negativeValues)
            for i in enumerate(absVal):
                if i == min(absVal):
                    absVal[Index] = 300000
        for a in range(len(values)):
            sum += int(values[a])
        print(sum)
    else:
        print("only", howMany, "cards accepted")
else:
    print("too many cards, error")
