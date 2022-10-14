'''
풀이 시작 시간: 2022-10-14 15:00
풀이 종료 시간: 2022-10-14 15:06

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.(1<=N, M<=100)
둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다.(1<=K<=100)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4

출력
첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
만약 X번 회사에 도달할 수 없다면 -1을 출력한다.
3

-1
'''
'''
- 플로이드 워셜 알고리즘을 활용하여 풀이
Pass/1st
'''

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            graph[i][j] = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

X, K = map(int, input().split())
for idx in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][idx] + graph[idx][j])

dist = graph[1][K] + graph[K][X]
if dist >= INF:
    print("-1")
else:
    print(dist)