def cardNumSearch(Amount, cardnum, givenCN, givenC):
    if Amount == len(cardnum):
        if givenCN == len(givenC):
            count = []
            cardnum.sort()
            begin_index = 0
            end_index = len(cardnum)-1
            for each in range(len(givenC)):
                if givenC[each] not in cardnum:
                    count.append(0)
                else:
                    while begin_index <= end_index:
                        midpoint = begin_index + (end_index - begin_index) // 2
                        midpoint_value = cardnum[midpoint]
                        if midpoint_value == givenC[each]:
                            cardnum.remove(givenC[each])
                        elif givenC[each] < midpoint_value:
                            end_index = midpoint - 1
                        elif givenC[each] > midpoint_value:
                            begin_index = midpoint + 1
            for each in count:
                print(each, end = ' ')
#                print(cardnum.count(each), end = ' ')

NoC = int(input())
cards = list(map(int, input().split(" ")))
provCN = int(input())
proC = list(map(int, input().split(" ")))
cardNumSearch(NoC, cards, provCN, proC)