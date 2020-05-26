def TinB():
    Np = int(input())
    Nt = list(map(int, input().split(" ")))
    if len(Nt) == Np:
        Lt = []
        Nt.sort()
        for each in range(Np):
            a = sum(Nt)
            Lt.append(a)
            Nt.remove(max(Nt))
    return sum(Lt)

print(TinB())