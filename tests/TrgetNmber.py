from itertools import product
def solution(numbers, target):
    answer = 0
    tupNN = []
    LoN = []
    negNum = (target - sum(numbers))/2
    for each in range(len(numbers)):
        if each == abs(negNum):
            answer += 1
            numbers.remove(each)
        else:
            pass
    for each in numbers:
        tupNN.append(-each)
    tupN = tuple(numbers)
    result = list(product(*tupN))
    for eachL in result:
        if sum(eachL) == abs(negNum):
            answer += 1
    return answer
solution([1, 1, 1, 1, 1], 3)