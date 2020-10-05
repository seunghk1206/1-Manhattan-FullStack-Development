def quadToDeci(num):
    if num >= 0:
        ans = 0
        a = str(num).split('.')[0][::-1]
        for each in range(len(a)):
            ans += int(a[each]) * 4**each
        if '.' in str(num):
            b = str(num).split('.')[1]
            for each in range(1, len(b)+1):
                ans += int(b[each-1]) * 4 ** (-1 * each)
        return ans
    elif num < 0:
        return -1 * quadToDeci(-num)
print(quadToDeci(0.1))