height = []
poss = []
for i in range(9):
    h = int(input())
    height.append(h)
varA = int(sum(height))
d = varA - 100
for each in range(len(height)):
    if height[each - 1] + height[each] == d:
        poss.append([height[each - 1], height[each]])
height.remove(poss[0][0])
height.remove(poss[0][1])
height.sort()
for each in height:
    print(each)