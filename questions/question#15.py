import itertools
a = int(input())

def prt(n):
    def threetie(mac, listI):
        result = [listI[i*mac:(i+1) * mac] for i in range((len(listI)+mac-1)//mac)]
        return result
    def squareB(inp):
        b = []
        countx = -2
        county = -2
        temp = []
        for each in range(inp):
            for eachNum in range(inp):
                temp.append('*')
            b.append(temp)
            temp = []
        for each in range(int(inp//3)):
            countx = 1
            for eachS in range(int(inp//3)):
                b[county][countx] = ' '
                countx += 3
            county += 3
        county = 1
        return b
    p = squareB(n)
    cnt = 0
    mlx = n
    for each in range(8):
        mlx /= 3
        if mlx > 1:
            cnt += 1
    x = n
    for each in range(cnt):
        squareB(int(qx))
        qx /= 3
        b = threetie(3, p)
    mx = itertools.chain(b)
    mx = threetie(n, mx)
    print('\n'.join([''.join([str(i) for i in row]) for row in mx]))

prt(a)