def solution(A):
    print(A)
    print(len(A))
    countList = []
    for each in range(len(A)):
        if A[each] == '1' or A[each] == '[1' or A[each] == '1]':
            a = A.count('6') * 2
            ln = len(A) - A.count('6') - A.count('1') - A.count('[1') - A.count('1]') - A.count('[6') - A.count('6]')
            countList.append(a + ln)
        elif A[each] == '2' or A[each] == '[2' or A[each] == '2]':
            a = A.count('5') * 2
            ln = len(A) - A.count('5') - A.count('2') - A.count('[2') - A.count('2]') - A.count('[5') - A.count('5]')
            countList.append(a + ln)
        elif A[each] == '3' or A[each] == '[3' or A[each] == '3]':
            a = A.count('4') * 2
            ln = len(A) - A.count('4') - A.count('3') - A.count('[3') - A.count('3]') - A.count('[4') - A.count('4]')
            countList.append(a + ln)
        elif A[each] == '4' or A[each] == '[4' or A[each] == '4]':
            a = A.count('3') * 2
            ln = len(A) - A.count('3') - A.count('4') - A.count('[4') - A.count('4]') - A.count('[3') - A.count('3]')
            countList.append(a + ln)
        elif A[each] == '5' or A[each] == '[5' or A[each] == '5]':
            a = A.count(2) * 2
            ln = len(A) -A.count('2') - A.count('5') - A.count('[5') - A.count('5]') - A.count('[2') - A.count('2]')
            countList.append(a + ln)
        elif A[each] == '6' or A[each] == '[6' or A[each] == '6]':
            a = A.count('1') * 2
            ln = len(A) -A.count('1') - A.count('6') - A.count('[6') - A.count('6]') - A.count('[1') - A.count('1]')
            countList.append(a + ln)
        else:
            pass
    print(countList)
    return min(countList)
XL = list(input().split(', '))
print(solution(XL))