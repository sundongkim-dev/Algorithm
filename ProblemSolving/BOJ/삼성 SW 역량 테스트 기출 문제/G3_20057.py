N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 토네이도 이동시 비율
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def move(cnt, dx, dy, direction):
    global answer, x, y

    for _ in range(cnt+1):
        x += dx
        y += dy
        # 범위 밖이면 stop
        if x < 0 or y < 0:
            break

        total = 0
        for dx, dy, z in direction:
            nx = x + dx
            ny = y + dy
            if z == 0:
                sand = graph[x][y] - total
            else:
                sand = int(graph[x][y] * z)
            if 0<=nx<N and 0<=ny<N:
                graph[nx][ny] += sand
            else:
                answer += sand
            total += sand
    


answer = 0
x, y = N//2, N//2

for i in range(N):
    if i%2 == 0:
        move(i, 0, -1, left)
        move(i, 1, 0, down)
    else:
        move(i, 0, 1, right)
        move(i, -1, 0, up)

print(answer)