'''
풀이 시작 시간: 2022-10-15 00:51
풀이 종료 시간: 2022-10-15 11:42

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
- 시간초과로 인해 dfs로 풀이
Pass/2nd
'''

import sys
sys.setrecursionlimit(100000) # 최대 재귀 한도를 늘린다.

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def solution():
    cnt = 0
    # 인접한 국가와의 인구 차이를 통해 연합 유무 탐색
    def dfs(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and check[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    check[nx][ny] = False
                    union.append([nx, ny])
                    dfs(nx, ny)

    while True:
        check = [[True] * N for _ in range(N)] # 탐색 유무
        flag = True
        for i in range(N):
            for j in range(N):
                union = []
                if check[i][j]:
                    union.append([i, j]) # 연합 나라 저장
                    check[i][j] = False
                    dfs(i, j)
                    # 연합의 개수가 2개 이상이라면,
                    if len(union) > 1:
                        flag = False
                        avg = sum([arr[x][y] for x, y in union]) // len(union)
                        for x, y in union:
                            arr[x][y] = avg
        # 연합의 개수가 2개 이상인 적이 없으면 종료
        if flag: 
            break

        cnt += 1

    return cnt

print(solution())