def DeciToTri(n, TargetNum):
    num = 3
    ans = ''
    hexaL = ["0", "1", "2"]
    if TargetNum >= 1:
        intP = str(TargetNum)
        if num**(n+1) > int(intP) >= num**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(num**abs(each-n))]
                intP = str((int(intP)%(num**abs(each-n))))
            return ans
        else:
            return DeciToTri(n+1, TargetNum)
    elif TargetNum == 0 or TargetNum == '0':
        return '.0' #이 문제에만 특화된 3진법 변환 코드

def triToDeci(num):
    ans = 0
    a = str(num)
    for each in range(len(a)):
        ans += int(a[each]) * 3 ** each
    return ans
def solution(n):
    return triToDeci(str(DeciToTri(0, n)))
print(solution(78413450))
#78413450 #110105530


