howMany = int(input("how many cards? "))
limit = int(input("what would you set as a limit? "))
absVal = []
EL = []
values = []
sum = 0
if 3 <= howMany <= 100:
    Cnumbers = list(input().split(', '))
    if len(Cnumbers) == howMany:
        Cnumbers.sort()
        for each in Cnumbers:
            EL.append(int(each) - int(limit))
        for each in EL:
            absVal.append(abs(each))
        for each in range(3):
            Index = int(absVal.index(min(absVal)))
            print(Cnumbers[Index])
            values.append(Cnumbers[Index])
            Cnumbers.remove(Cnumbers[Index])
            absVal.remove(absVal[Index])
        for a in range(len(values)):
            sum += int(values[a])
        print(sum)
    else:
        print("only", howMany, "cards accepted")
else:
    print("too many cards, error")