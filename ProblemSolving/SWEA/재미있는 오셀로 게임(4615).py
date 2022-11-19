'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 20:44
풀이 종료 시간: 2022-11-19 21:05

시간 제한: 30개/4초
메모리 제한: 256MB

입력: 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.
돌의 색이 1이면 흑돌, 2이면 백돌이다.
만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.
돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

출력: 
각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.

제한사항:

풀이: 
1st / 8가지 방향에 대해 계산

제출 이력:
1st / Pass
'''

direction = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    graph = [[0]*N for _ in range(N)]
    graph[N//2-1][N//2-1] = 2
    graph[N//2-1][N//2] = 1
    graph[N//2][N//2-1] = 1
    graph[N//2][N//2] = 2
    
    for cmd in range(M):
        y, x, color = map(int, input().split())
        x -= 1
        y -= 1
        if not graph[x][y]:
            graph[x][y] = color
            for i in range(8):
                dx, dy = direction[i]
                nx, ny = x + dx, y + dy
                rev = []
                while True:
                    if nx<0 or N-1<nx or ny<0 or N-1<ny:
                        rev = []
                        break
                    if graph[nx][ny] == 0:
                        rev = []
                        break
                    if graph[nx][ny] == color:
                        break
                    else:
                        rev.append((nx, ny))
                    nx += dx
                    ny += dy
                for rx, ry in rev:
                    graph[rx][ry] = color
    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                W += 1
            elif graph[i][j] == 2:
                B += 1     
    
    print("#{} {} {}".format(tc, W, B))