'''
풀이 시작 시간: 2022-10-17 14:11
풀이 종료 시간: 2022-10-17 14:24

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방햔 d가 각각 서로 공백으로 구분하여 주어진다. 
방향 d의 값으로는 다음과 같이 4가지가 존재한다.
0 : 북쪽
1 : 동쪽
2 : 남쪽
3 : 서쪽
셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. 
N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 
맵의 외각은 항상 바다로 되어 있다.
0 : 육지
1 : 바다
처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
4 4
1 1 0 // (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

출력
첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
3

풀이
문제의 분기에 따라 구현해주면 된다.
'''

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[x][y] = 1

def turn_left():
    global d
    d = (d-1)%4

answer = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(answer)