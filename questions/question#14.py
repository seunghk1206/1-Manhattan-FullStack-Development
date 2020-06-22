N = int(input())
LoL = []
LoB = []
for each in range(N):
    a = int(input())
    LoL.append(a)
LoL.sort()
for each in range(1, len(LoL)):
    LoB.append(max(LoL)*each)
    LoL.remove(max(LoL))
print(max(LoB))