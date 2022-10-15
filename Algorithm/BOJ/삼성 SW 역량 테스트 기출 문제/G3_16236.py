import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

x, y, time, curSize, ans = 0, 0, 0, 2, 0
food = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j

def biteFish(x, y, shark_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    tmp = []

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if arr[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy]+1
                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0:
                        tmp.append((nx,ny,distance[nx][ny]))
    return sorted(tmp, key=lambda x : (-x[2], -x[0], -x[1]))

cnt = 0
while True:
    shark = biteFish(x, y, curSize)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()
    ans += dist
    arr[x][y], arr[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == curSize:
        curSize +=1
        cnt = 0

print(ans)