from collections import deque
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
gap = 2**N
graph = [list(map(int, input().split())) for _ in range(gap)]
L = list(map(int, input().split()))


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for level in L:
    level_gap = 2**level
    rotated_graph = [[0]*gap for _ in range(gap)]
    # 부분 격자로 나눈다
    for i in range(0, gap, level_gap):
        for j in range(0, gap, level_gap):
            # 모든 부분 격자 시계 방향으로 90도 회전
            for x in range(level_gap):
                for y in range(level_gap):
                    rotated_graph[i+y][j+level_gap-x-1] = graph[i+x][j+y]
    # 얼음 녹이기
    graph = [[0]*gap for _ in range(gap)]
    for x in range(gap):
        for y in range(gap):
            cnt = 0
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if 0<=nx<gap and 0<=ny<gap and rotated_graph[nx][ny] != 0: # 얼음 있는 칸 세기
                    cnt += 1
            if rotated_graph[x][y] > 0:
                # 얼음이 있는 칸 3개
                if cnt < 3:
                    graph[x][y] = rotated_graph[x][y]-1
                else:
                    graph[x][y] = rotated_graph[x][y]

# 가장 큰 덩어리 구하기
visited = [[0]*gap for _ in range(gap)]
answer = 0
ice_list = [0]
for i in range(gap):
    for j in range(gap):
        tmp = []
        if graph[i][j] != 0 and visited[i][j] == 0:
            tmp.append((i, j))
            visited[i][j] = 1
            answer += graph[i][j]
            cnt = 1
            while tmp:
                a, b = tmp.pop()
                for idx in range(4):
                    nx, ny = a+dx[idx], b+dy[idx]
                    if 0<=nx<gap and 0<=ny<gap and visited[nx][ny] == 0 and graph[nx][ny] != 0:
                        tmp.append((nx, ny))
                        visited[nx][ny] = 1
                        answer += graph[nx][ny]
                        cnt += 1
            ice_list.append(cnt)

print(answer)
print(max(ice_list))