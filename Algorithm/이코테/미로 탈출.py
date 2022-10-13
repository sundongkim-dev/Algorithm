'''
풀이 시작 시간: 2022-10-13 21:07
풀이 종료 시간: 2022-10-13 21:18

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 두 정수 N,M(4<=N,M<=200)이 주어집니다.
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
5 6
101010
111111
000001
111111
111111

출력
첫째 줄에 최소 이동 칸의 개수를 출력한다.
10
'''

'''
- [0,0]에서부터 BFS 호출
'''

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

queue = deque()
queue.append([0,0])
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<M:
            if visited[nx][ny] == False and miro[nx][ny]==1:
                miro[nx][ny] = miro[x][y] + 1
                visited[nx][ny] = True
                queue.append([nx, ny])

print(miro[N-1][M-1])