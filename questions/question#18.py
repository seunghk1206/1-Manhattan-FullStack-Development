def solution(array, commands):
    answer = [sorted(array[each[0]-1:each[1]])[each[2]-1] for each in commands]
    return answer
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))