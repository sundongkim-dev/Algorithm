'''
출처: https://www.acmicpc.net/problem/16234

풀이 시작 시간: 2022-11-10 19:39
풀이 종료 시간: 2022-11-08 20:44

시간 제한: 2초
메모리 제한: 512MB

입력: 
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력: 
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

제한사항:

풀이: 
1st / dfs로 구현한다.
2nd / 최대 재귀 한도 100,000으로 늘리기
3rd / BFS로 구현
제출 이력: 
1st / RecursionError
2nd / Pass
3rd / Pass
'''

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    n,l,r = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)]
    cnt = 0
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    # 격자 모양으로 탐색
    cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])
    
    while True:
        q = deque()
        for _ in range(len(cand)):
            i,j = cand.popleft()
            if visited[i][j] == cnt:
                continue
            visited[i][j] = cnt
            area = set([(i,j)])
            popul = board[i][j]
            q.append((i,j))
            
            # BFS
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx=x+a; dy=y+b
                    if dx>=n or dx<0 or dy>=n or dy<0 or visited[dx][dy] == cnt:
                        continue

                    if l<=abs(board[x][y]-board[dx][dy])<=r:
                        visited[dx][dy] = cnt
                        area.add((dx,dy))
                        popul += board[dx][dy]
                        q.append((dx,dy))
            
            # 국경선이 열린 경우
            if len(area) > 1:
                avg_popul = popul//len(area)
                for x,y in area:
                    board[x][y] = avg_popul
                    cand.append((x,y))
        if cand:
            cnt += 1
        else:
            break
    return cnt
    
answer = solution()
print(answer)


# import sys
# sys.setrecursionlimit(100000) # 최대 재귀 한도를 늘린다.

# N, L, R = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# answer = 0

# def dfs(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<N and 0<=ny<N and check[nx][ny]:
#             if L<=abs(graph[x][y] - graph[nx][ny])<=R:
#                 check[nx][ny] = False
#                 union.append((nx, ny))
#                 dfs(nx, ny)
    
# while True:
#     check = [[True]*N for _ in range(N)]
#     flag = True
#     for i in range(N):
#         for j in range(N):
#             union = []
#             if check[i][j]:
#                 union.append((i, j))
#                 check[i][j] = False
#                 dfs(i, j)
                
#                 if len(union) > 1:
#                     flag = False
#                     avg = sum([graph[x][y] for x,y in union]) // len(union)
#                     for x, y in union:
#                         graph[x][y] = avg
#     if flag:
#         break
    
#     answer += 1

# print(answer)