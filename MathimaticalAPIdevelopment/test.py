def printDataN(n):
    print("Analysis datas available: ", n)
printDataN(1000)
printDataN(1000)
printDataN(1000)
printDataN(1000)
printDataN(1000)
printDataN(1000)
printDataN(1000)

class math():
    pi = 3.14159265
    e = 2.718
    def sqrt(self, n):
        return n**(1/2)
    def areaOfCircle(self, r):
        return self.pi*r**2
    def volumeOfSphere(self, r):
        return 4/3*self.pi*r**3
    def volumeOfCylinder(self, r, h):
        return (self.pi*r**2)*h
    def surfaceAreaOfSphere(self, r):
        return 4*self.pi*r**2
    def versatileDeci(self, n, TargetNum, num):
        a = []
        for each in range(num):
            a.append('(' + str(each) + ')')
        ans = ''
        hexaL = a
        if float(TargetNum) >= 1:
            intP = str(TargetNum).split('.')[0]
            if num**(n+1) > int(intP) >= num**n:
                for each in range(n+1):
                    ans += hexaL[int(intP)//(num**abs(each-n))]
                    intP = str((int(intP)%(num**abs(each-n))))
                try:
                    decP = str(TargetNum).split('.')[1]
                    decP = '0.' + decP
                    return ans + '.' + versatileDeci(-1, float(decP), num)
                except:
                    return ans
            else:
                return self.versatileDeci(n+1, TargetNum, num)
        elif float(TargetNum) < 0:
            return '-' + self.versatileDeci(0, -TargetNum, num)
        elif float(TargetNum) == 0 or TargetNum == '0':
            return '0'
        elif 1 > float(TargetNum) > 0:
            if num**(n+1) > TargetNum >= num**n:
                if TargetNum%(num**n) == 0:
                    return hexaL[int(TargetNum//(num**n))]
                return hexaL[int(TargetNum//(num**n))] + self.versatileDeci(n-1, TargetNum%(num**n), num)
            else:
                return '0' + self.versatileDeci(n-1, TargetNum, num)
    def factorial(self, x):
        if x == 0:
            return 1
        else: 
            return x * self.factorial(x-1)
    def f(self, x, n):
        return (((-1)**n)*x**(2*n+1)/self.factorial(2*n+1))
    def sin(self, x, n):
        if x%90 == 0:
            if (x//90)%2 == 1:
                if ((x//90)//2)%2 == 1:
                    return -1
                else: 
                    return 1
            else:
                return 0
        else:
            pi2deg = self.pi/180
            if n == 0:
                return self.f(x*pi2deg, n)
            else:
                return self.f(x*pi2deg, n) + self.sin(x,n-1)
    def g(self, x, n):
        return (((-1)**n)*x**(2*n)/self.factorial(2*n))
    def cos(self, x, n):
        if x%90 == 0:
            if (x//90)%2 == 1:
                return 0
            else:
                if x%360 == 0:
                    return 1
                else:
                    return -1
        else:
            pi2deg = 3.1415/180
            if n == 0:
                return self.g(x*pi2deg, n)
            else:
                return self.g(x*pi2deg, n) + self.cos(x,n-1)
    def tan(self, x, n):
        return self.sin(x, n)/self.cos(x, n)
print(math.sqrt(84))