class simpAngMo:
    def __init__(self, m, r, v):
        self.m = m
        self.r = r
        self.v = v
    def getAngVel(self):
        return str(self.v/self.r) + ' rad s^(-1)'
    def getCentAcc(self):
        return str(self.v**2/self.r) + ' m s^(-2)'
    def getCentAngAcc(self):
        return str(self.magnitudeOf(self.getCentAcc())/self.r) + ' rad s^(-2)'
    def centF(self):
        return str(self.m * self.magnitudeOf(self.getCentAcc())) + ' N'
    
    def magnitudeOf(self, string):
        return float(string.split(' ')[0])

class physAngMo:
    def __init__(self, m, shape, r, v):
        self.m = m
        self.r = r
        self.v = v
        if shape == 'Sphere':
            self.MoI = (self.m*self.r**2)*2/5
        elif shape == 'FullCylinder':
            self.MoI = (self.m*self.r**2)
        elif shape == 'HollowCylinder':
            self.MoI = (self.m*self.r**2)/2
        elif shape == 'Stick':
            self.MoI = (self.m*self.r**2)/12
        else:
            self.MoI = shape*(self.m*self.r**2)
    def KEget(self):
        return str(self.m*self.v**2/2+(self.MoI*self.v**2)/(2*self.r**2)) + ' J'

a = simpAngMo(5, 2, 10)
b = physAngMo(5, 10, 2, 10)
print(a.centF())
print(b.KEget())