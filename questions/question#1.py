
def chessBoardCheck():
    BWlist = []
    n = 0
    y, x = map(int, input().split())
    for i in range(y):
        a = input()
        BWlist.append(a)
        if len(a) != x:
            print("not a right length!")
            break
    for i in range(y):
        for each in range(x):
            if BWlist[i][0] != BWlist[i-1][0]:
                if BWlist[i][0] == 'W':
                    if each % 2 == 0:
                        if BWlist[i][each] != 'W':
                            n += 1
                    elif each % 2 == 1:
                        if BWlist[i][each] != 'B':
                            n += 1
                elif BWlist[i][0] == 'B':
                    if each % 2 == 0:
                        if BWlist[i][each] != 'B':
                            n += 1
                    elif each % 2 == 1:
                        if BWlist[i][each] != 'W':
                            n += 1
            else:
                if BWlist[i][0] == 'W':
                    if each % 2 == 0:
                        if BWlist[i][each] != 'B':
                            n += 1
                    elif each % 2 == 1:
                        if BWlist[i][each] != 'W':
                            n += 1
                elif BWlist[i][0] == 'B':
                    if each % 2 == 0:
                        if BWlist[i][each] != 'W':
                            n += 1
                    elif each % 2 == 1:
                        if BWlist[i][each] != 'B':
                            n += 1
    return n

print(chessBoardCheck())