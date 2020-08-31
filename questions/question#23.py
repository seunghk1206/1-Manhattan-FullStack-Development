def solution(array, commands):
    answer = [sorted(array[each[0]-1:each[1]])[each[2]-1] for each in commands]
    return answer