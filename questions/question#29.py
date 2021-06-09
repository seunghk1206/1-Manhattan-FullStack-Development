n = int(input())
print((9**3*4-621)*n)

coordinate = str(input())
strL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numcoor = [strL.index(coordinate[0])+1, int(coordinate[1])]
possibility = 0
if numcoor[0]-2 >= 1 and numcoor[1]+1 >= 1:
    possibility+=1
if numcoor[0]-2 >= 1 and numcoor[1]-1 >= 1:
    possibility+=1
if numcoor[0]+2 >= 1 and numcoor[1]+1 >= 1:
    possibility+=1
if numcoor[0]+2 >= 1 and numcoor[1]-1 >= 1:
    possibility+=1
if numcoor[0]+1 >= 1 and numcoor[1]+2 >= 1:
    possibility+=1
if numcoor[0]-1 >= 1 and numcoor[1]+2 >= 1:
    possibility+=1
if numcoor[0]+1 >= 1 and numcoor[1]-2 >= 1:
    possibility+=1
if numcoor[0]-1 >= 1 and numcoor[1]-2 >= 1:
    possibility+=1
print(possibility)