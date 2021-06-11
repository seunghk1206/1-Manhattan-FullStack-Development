def BFS(M, arr, babSharkSize):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    a = arr
    visit = [[False] * M for _ in range(M)]
    distance = [[0] * M for _ in range(M)]

    queue = []
    for each in range(M):
        arr[each].index(9)
    queue.append((0,0))
    visit[0][0]
    distance[0][0] = 1

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < M:
                if visit[nx][ny] == False and a[nx][ny] <= babSharkSize:
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y]+1
                    visit[nx][ny] = True
    return distance
arraySize = int(input())
arr = []
for each in range(arraySize):
    L = list(map(int, input().split()))
    arr.append(L)

initBabSharkSize = 2
for each in arr:
    for eachNum in each:
        if 0 < eachNum < initBabSharkSize:
            BFS(arraySize, arr, initBabSharkSize)