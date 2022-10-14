'''
풀이 시작 시간: 2022-10-14 18:10
풀이 종료 시간: 2022-10-14 19:04

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)
둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력
로봇 청소기가 청소하는 칸의 개수를 출력한다.
'''

'''
- 본문 그대로 구현
Fail/1st
- 인덱스 에러, 인덱스 유효성 검사 추가
Fail/2nd
- 인덱스 에러, visited 잘못 선언
Pass/3rd
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())

place = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 현재 위치를 청소한다
answer = 1
visited[r][c] = True
while True:
    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
    for idx in range(4):
        d -= 1
        if d < 0:
            d = 3
        nr = r + dx[d]
        nc = c + dy[d]
        # 인덱스 유효성 검사
        if nr >= N and nr < 0 and nc >=M and nc < 0:
            continue
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 전진하고 다시 1번
        if visited[nr][nc] == False and place[nr][nc] == 0:
            visited[nr][nc] = True
            answer += 1
            r = nr; c = nc
            break
        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 다시 탐색
        else:
            continue
    # 왼쪽 방향에 청소할 공간이 없다면
    else:
        # 후진 가능한가?
        i = d - 2
        if i < 0:
            i += 4
        nr = r + dx[i]
        nc = c + dy[i]

        # 인덱스 유효성 검사, 후진 불가능하면,
        if nr >= N and nr < 0 and nc >=M and nc < 0 or place[nr][nc] == 1:
            break
        # 후진 가능하면 후진한다
        else:
            r = nr
            c = nc

print(answer)