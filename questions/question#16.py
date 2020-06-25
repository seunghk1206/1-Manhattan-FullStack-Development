inp = int(input())
LoN = []
for i in range(inp):
    inp2 = int(input())
    if inp2 == 0: LoN.remove(LoN[-1])
    else: LoN.append(inp2)
print(sum(LoN))