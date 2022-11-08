'''
풀이 시작 시간: 2022-10-13 20:42
풀이 종료 시간: 2022-10-13 21:03

시간 제한 1초
메모리 제한 128MB

입력
첫 번째 줄에 얼음 틀의 세로 길이 N가 가로 길이 M이 주어진다.
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
4 5
00110
00011
11111
00000

출력
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

3
'''

'''
- [0,0]부터 [N, M]까지 각 지점마다 dfs 호출해서 개수 세어주기
'''

N, M = map(int, input().split())
iceFrame = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
answer = 0

def dfs(x, y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    # 아직 방문하지 않은 지점이라면
    if visited[x][y] == False and iceFrame[x][y] == 0:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            answer += 1

print(answer)