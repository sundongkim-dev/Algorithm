'''
풀이 시작 시간: 2022-10-15 15:01
풀이 종료 시간: 2022-10-15 15:29

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
'''

'''
- bfs 활용해서 시뮬레이션 반복
Pass/1st (pyp3)
'''
from collections import deque
import copy, sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    tmp_arr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                q.append((i,j))
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                q.append((nx, ny))
    
    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_arr[i].count(0)

    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

answer = 0
wall(0)
print(answer)