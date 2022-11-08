'''
풀이 시작 시간: 2022-10-15 02:14
풀이 종료 시간: 2022-10-15 02:36

시간 제한 1초
메모리 제한 1024MB

입력
첫째 줄에 N, M이 주어진다.
둘째 줄부터 N개의 줄에는 N개의 정수가 주어진다. r번째 행의 c번째 정수는 A[r][c]를 의미한다.
다음 M개의 줄에는 이동의 정보 di, si가 순서대로 한 줄에 하나씩 주어진다.

출력
첫째 줄에 M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 출력한다.
'''

'''
- 시뮬레이션
Pass/1st
'''

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
moves = []
for i in range(M):
    tmp = list(map(int, input().split()))
    moves.append([tmp[0] - 1, tmp[1]])

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

for i in range(M):

    move = moves[i]
    next_clouds = []
    for cloud in clouds:
        x = cloud[0]; y = cloud[1]
        d = move[0]; s = move[1]
        nx = (N + x + dx[d] * s) % N
        ny = (N + y + dy[d] * s) % N
        next_clouds.append([nx, ny])

    visited = [[False]* N for _ in range(N)]
    for cloud in next_clouds:
        x = cloud[0]; y = cloud[1]
        li[x][y] += 1
        visited[x][y] = True
    
    clouds = []

    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]; y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]
            if 0 <= nx < N and 0<= ny < N and li[nx][ny] >= 1:
                count += 1

        li[x][y] += count

    for i in range(N):
        for j in range(N):
            if li[i][j] >= 2 and visited[i][j] == False:
                li[i][j] -= 2
                clouds.append([i, j])

ans = 0
for i in range(N):
    ans += sum(li[i])

print(ans)