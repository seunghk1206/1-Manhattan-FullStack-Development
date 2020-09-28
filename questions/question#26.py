def solution(arrows):
    answer = 0
    tempL = []
    coorL = [[0,0]]
    for each in arrows:
        if each == 0: coorL.append([int(coorL[-1][0]), int(coorL[-1][1])+1])
        elif each == 1: coorL.append([int(coorL[-1][0])+1, int(coorL[-1][1])+1])
        elif each == 2: coorL.append([int(coorL[-1][0])+1, int(coorL[-1][1])])
        elif each == 3: coorL.append([int(coorL[-1][0])+1, int(coorL[-1][1])-1])
        elif each == 4: coorL.append([int(coorL[-1][0]), int(coorL[-1][1])-1])
        elif each == 5: coorL.append([int(coorL[-1][0])-1, int(coorL[-1][1])-1])
        elif each == 6: coorL.append([int(coorL[-1][0])-1, int(coorL[-1][1])])
        elif each == 7: coorL.append([int(coorL[-1][0])-1, int(coorL[-1][1])+1])
    for each in coorL:
        if each in tempL:
            answer += 1
        tempL.append(each)
    return answer
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))