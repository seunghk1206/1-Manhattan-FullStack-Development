def quadToDeci(num):
    ans = 0
    a = str(num).split('.')[0][::-1]
    for each in range(len(a)):
        ans += int(a[each]) * 4**each
    if '.' in str(num):
        b = str(num).split('.')[1]
        for each in range(len(b)):
            pass