def solution(arrows):
    answer = 0
    coorL = [[0,0]]
    for each in arrows:
        if each == 0: 
            a = [int(coorL[-1][0]), int(coorL[-1][1])+1]
        elif each == 1: 
            a = [int(coorL[-1][0])+1, int(coorL[-1][1])+1]
        elif each == 2: 
            a = [int(coorL[-1][0])+1, int(coorL[-1][1])]
        elif each == 3: 
            a = [int(coorL[-1][0])+1, int(coorL[-1][1])-1]
        elif each == 4: 
            a = [int(coorL[-1][0]), int(coorL[-1][1])-1]
        elif each == 5: 
            a = [int(coorL[-1][0])-1, int(coorL[-1][1])-1]
        elif each == 6: 
            a = [int(coorL[-1][0])-1, int(coorL[-1][1])]
        elif each == 7: 
            a = [int(coorL[-1][0])-1, int(coorL[-1][1])+1]
        if a in coorL:
            answer += 1
        coorL.append(a)
    return answer
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0, 2, 4]))
#ans = 5