import copy
import sys; input = sys.stdin.readline


R, C, M = map(int, input().split())

directions = [(-1,0), (1,0), (0, 1), (0, -1)]

graph = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1].append([s, d-1, z])

answer = 0
# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다
king = -1

while king < C-1:
    # 1초 동안 다음의 일이 일어난다
    # step1. 낚시왕이 오른쪽으로 한 칸 이동
    king += 1
    # step2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for i in range(R):
        if graph[i][king]: # 상어가 열에 있다면 잡기
            answer += graph[i][king][0][2]
            graph[i][king].pop()
            break
    # step3. 상어가 이동한다.
    new_board = [[[] for _ in range(C)] for _ in range(R)]  # 상어들의 새 위치를 담을 공간
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j].pop()
                dist = s
                while 0 < dist:
                    nx = x + directions[d][0]
                    ny = y + directions[d][1]
                    if 0<=nx<R and 0<=ny<C:
                        x, y = nx, ny
                        dist -= 1
                    else:
                        if d == 0 or d == 2: # 상 우
                            d += 1
                        elif d == 1 or d == 3: # 하 좌
                            d -= 1
                        continue
                new_board[x][y].append([s, d, z])
    graph = new_board

    # step4. 상어가 이동을 마친 후에 한 칸에 두 마리 이상 있으면 크기가 가장 큰 상어가 다 잡아먹는다
    for i in range(R):
        for j in range(C):
            if len(graph[i][j]) > 1:
                graph[i][j].sort(key=lambda x : x[2], reverse=True)
                while 1 < len(graph[i][j]):
                    graph[i][j].pop()

# 낚시왕이 잡은 상어 크기의 합은?
print(answer)