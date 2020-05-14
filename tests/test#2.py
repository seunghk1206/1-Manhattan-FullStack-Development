def solution(A):
    countList = []
    for each in range(len(A)):
        count = 0
        m = 0
        n = 0
        if A[each] == 1:
            a = A.count(6) * 2
            m = count + a
            b = A.count(1)
            ln = len(A) - a/2 - b
            n = m + ln
        elif A[each] == 2:
            a = A.count(5) * 2
            m = count + a
            b = A.count(2)
            ln = len(A) - a/2 - b
            n = m + ln
        elif A[each] == 3:
            a = A.count(4) * 2
            m = count + a
            b = A.count(3)
            ln = len(A) - a/2 - b
            n = m + ln
        elif A[each] == 4:
            a = A.count(3) * 2
            m = count + a
            b = A.count(4)
            ln = len(A) - a/2 - b
            n = m + ln
        elif A[each] == 5:
            a = A.count(2) * 2
            m = count + a
            b = A.count(5)
            ln = len(A) - a/2 - b
            n = m + ln
        elif A[each] == 6:
            a = A.count(6) * 2
            m = count + a
            b = A.count(1)
            ln = len(A) - a/2 - b
            n = m + ln
        countList.append(n)
    return min(countList)
XL = input()
print(solution(XL))

##



def Rsolution(A):
    countList = []
    count = 0
    for each in range(len(A)):
        for i in range(len(A)):
            if A[each] == 1 and A[i] == 6:
                count += 2
            elif A[each] == 2 and A[i] == 5:
                count += 2
            elif A[each] == 3 and A[i] == 4:
                count += 2
            elif A[each] == 4 and A[i] == 3:
                count += 2
            elif A[each] == 5 and A[i] == 2:
                count += 2
            elif A[each] == 6 and A[i] == 1:
                count += 2
            elif A[each] == A[i]:
                count += 0
            else:
                count += 1
        countList.append(count)
        count = 0
    return min(countList)
m = input()
print(Rsolution(m))
