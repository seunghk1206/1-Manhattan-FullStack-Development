class AngMo:
    def __init__(self, r, v):
        self.r = r
        self.v = v
    def getAngVel(self):
        return str(self.v/self.r) + ' rad s^(-1)'
    def getCentAcc(self):
        return str(self.v**2/self.r) + ' m s^(-2)'
    def getCentAngAcc(self):
        return str(self.magnitudeOf(self.getCentAcc())/self.r) + ' rad s^(-2)'
    def magnitudeOf(self, string):
        return float(string.split(' ')[0])

a = AngMo(2, 10)
print(a.getCentAngAcc())