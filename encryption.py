howMany = int(input("how many individual units of letters? "))
independentLetters = []
Len = []
Len2 = []
for each in range(howMany):
    inputUnit = input().split()
    print(inputUnit)
    inputLen = len(inputUnit)
    independentLetters.extend(inputUnit)
    print(independentLetters)
    Len.append(inputLen)
    print(Len)
for i in range(howMany):
    for each in range(Len[i]):
        Len2.append(Len[i]-1)
        print(Len2)
for each in range(0, len(independentLetters)):
    Index = independentLetters[each]
    length = independentLetters.index(Index)
    if length != Len2[each]:
        if Index == 'ㄱ':
            a = 1
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㄴ':
            a = 2
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㄷ':
            a = 3
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㄹ':
            a = 4
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅁ':
            a = 5
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅂ':
            a = 6
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅅ':
            a = 7
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅇ':
            a = 8
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅈ':
            a = 9
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅊ':
            a = 10
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅋ':
            a = 11
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅌ':
            a = 12
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅍ':
            a = 13
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅎ':
            a = 14
            x = format(a, 'b')
            print(x, "+")
        elif Index == 'ㅏ':
            a = "R1"
            print(a, "+")
        elif Index == 'ㅑ':
            a = "R2"
            print(a, "+")
        elif Index == 'ㅓ':
            a = "L1"
            print(a, "+")
        elif Index == 'ㅕ':
            a = "L2"
            print(a, "+")
        elif Index == 'ㅗ':
            a = "U1"
            print(a, "+")
        elif Index == 'ㅛ':
            a = "U2"
            print(a, "+")
        elif Index == 'ㅜ':
            a = "D1"
            print(a, "+")
        elif Index == 'ㅠ':
            a = "D2"
            print(a, "+")
        elif Index == 'ㅡ':
            a = "RUDL1"
            print(a, "+")
        elif Index == 'ㅣ':
            a = "RUDL2"
            print(a, "+")
        elif Index == 'ㅐ':
            a = "R1 + RUDL2"
            print(a, "+")
        elif Index == 'ㅔ':
            a = "L1 + RUDL2"
            print(a, "+")
        elif Index == 'ㅖ':
            a = "L2 + RUDL2"
            print(a, "+")
        elif Index == 'ㅒ':
            a = "R2 + RUDL2"
            print(a, "+")
    elif length == Len2[each]:
        if Index == 'ㄱ':
            a = 1
            x = format(a, 'b')
            print(x)
        elif Index == 'ㄴ':
            a = 2
            x = format(a, 'b')
            print(x)
        elif Index == 'ㄷ':
            a = 3
            x = format(a, 'b')
            print(x)
        elif Index == 'ㄹ':
            a = 4
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅁ':
            a = 5
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅂ':
            a = 6
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅅ':
            a = 7
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅇ':
            a = 8
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅈ':
            a = 9
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅊ':
            a = 10
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅋ':
            a = 11
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅌ':
            a = 12
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅍ':
            a = 13
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅎ':
            a = 14
            x = format(a, 'b')
            print(x)
        elif Index == 'ㅏ':
            a = "R1"
            print(a)
        elif Index == 'ㅑ':
            a = "R2"
            print(a)
        elif Index == 'ㅓ':
            a = "L1"
            print(a)
        elif Index == 'ㅕ':
            a = "L2"
            print(a)
        elif Index == 'ㅗ':
            a = "U1"
            print(a)
        elif Index == 'ㅛ':
            a = "U2"
            print(a)
        elif Index == 'ㅜ':
            a = "D1"
            print(a)
        elif Index == 'ㅠ':
            a = "D2"
            print(a)
        elif Index == 'ㅡ':
            a = "RUDL1"
            print(a)
        elif Index == 'ㅣ':
            a = "RUDL2"
            print(a)
        elif Index == 'ㅐ':
            a = "R1 + RUDL2"
            print(a)
        elif Index == 'ㅔ':
            a = "L1 + RUDL2"
            print(a)
        elif Index == 'ㅖ':
            a = "L2 + RUDL2"
            print(a)
        elif Index == 'ㅒ':
            a = "R2 + RUDL2"
            print(a)