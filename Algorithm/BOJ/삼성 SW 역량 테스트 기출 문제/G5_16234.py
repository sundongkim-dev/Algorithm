'''
풀이 시작 시간: 2022-10-15 00:51
풀이 종료 시간: 2022-10-15 01:41

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
'''

'''
- bfs 활용해서 시뮬레이션 반복
Fail/1st
- 시간초과
'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(a, b):
    q = deque()
    q.append([a,b])
    tmp = []
    tmp.append([a,b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    tmp.append([nx, ny])
    return tmp

answer = 0
while True:
    visited = [[False]*N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                li = bfs(i, j)
                if len(li) > 1:
                    flag = True
                    num = sum([arr[x][y] for x, y in li]) // len(li)
                    for x, y in li:
                        arr[x][y] = num
    if flag == False:
        break
    answer += 1

print(answer)
