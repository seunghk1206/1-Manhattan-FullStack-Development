def solution(board, moves):
    dummy = []
    electedList = []
    answer = 0
    for i in moves:
        for each in range(0, len(board[0])):
            if board[each][i-1] > 0:
                dummy.append(board[each][i-1])
        if len(dummy) == 0:
            print("nothing left there!")
        elif len(dummy) != 0:
            electedList.append(dummy[0])
        for each in range(len(board[0])):
            if board[each][i-1] > 0:
                board[each][i-1] = 0
                break
        dummy = []
        for each in range(1, len(electedList)):
            if electedList[each-1] == electedList[each]:
                if electedList[each] not in electedList:
                    pass
                elif electedList[each-1] not in electedList:
                    pass
                else:
                    electedList.remove(electedList[each])
                    electedList.remove(electedList[each-1])
                    answer += 2
    print("answer:", answer)
    return answer


a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]
solution(a, b)