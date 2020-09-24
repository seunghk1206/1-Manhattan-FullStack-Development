'''
def solution(k, room_number):
    answer = []
    numL = [each for each in range(1, len(room_number)+1)]
    print(numL)
    for each in room_number:
        if each in numL:
            answer.append(each)
            numL.remove(each)
        elif each not in numL:
            answer.append(min(numL))
            numL.remove(min(numL))
    return answer
print(solution(10, [1,3,4,1,3,1]))
'''
import sys

sys.setrecursionlimit(10000000)


def recursionfindroom(room, reservation):
    if room not in reservation:
        reservation[room] = room + 1
        return room
    empty= recursionfindroom(reservation[room], reservation)
    reservation[room]=empty+1
    return empty

def solution(k, room_number):
    answer = []
    reservation = {}
    for i in room_number:
        answer.append(recursionfindroom(i, reservation))

    return answer
print(solution(10, [1,3,4,1,3,1]))