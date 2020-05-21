def binary_search():
    intLst = []
    intLst2 = []
    a = int(input())
    for i in range(a):
        intLst.append(int(input()))
    intLst.sort()
    b = int(input())
    for i in range(b):
        intLst2.append(int(input()))
    print(intLst, intLst2)
    begin_index = 0
    end_index = len(intLst)-1
    for i in range(len(intLst2)):
        while begin_index <= end_index:
            midpoint = begin_index + (end_index - begin_index) // 2
            midpoint_value = intLst[midpoint]
            if midpoint_value == intLst2[i]:
                print('1')
            elif intLst2[i] < midpoint_value:
                end_index = midpoint - 1
            elif intLst2[i] > midpoint_value:
                begin_index = midpoint + 1
            else:
                print('0')
    return None

binary_search()

##ans
n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

def bin_tree(s, n, st, en):
    if st > en:
        return 0
    mid = (st + en)//2
    if s[mid] > n:
        return bin_tree(s, n, st, mid-1)
    elif s[mid] < n:
        return bin_tree(s, n, mid+1, en)
    else: 
        return 1

a1.sort()
for i in a2:
    print(bin_tree(a1, i, 0, n-1))