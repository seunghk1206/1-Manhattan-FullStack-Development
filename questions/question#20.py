def solution(answers):
    answer2 = []
    count1 = 0
    count2 = 0
    count3 = 0
    type1 = [1,2,3,4,5]
    type2 = [2,1,2,3,2,4,2,5]
    type3 = [3,3,1,1,2,2,4,4,5,5]
    while True:
        type1.extend(type1)
        type2.extend(type2)
        type3.extend(type3)
        if len(type1) >= len(answers) and len(type2) >= len(answers) and len(type3) >= len(answers):
            break
    for each in range(len(answers)):
        if answers[each] == type1[each]:
            count1 += 1
        if answers[each] == type2[each]:
            count2 += 1
        if answers[each] == type3[each]:
            count3 += 1
    answer = [count1, count2, count3]
    x = max(answer)
    if x == count1:
        answer2.append(1)
    if x == count2:
        answer2.append(2)
    if x == count3:
        answer2.append(3)
    return answer2