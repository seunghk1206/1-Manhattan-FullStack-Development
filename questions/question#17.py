n = int(input())
def P(inp):
    LoL = ['수', '박']
    for _ in range(inp//2):
        print(LoL[0])
        print(LoL[1])
    if inp%2 == 1:
        print(LoL[0])
P(n)