'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 18:44
풀이 종료 시간: 2022-11-19 19:31

시간 제한: 10개/4초
메모리 제한: 256MB

입력: 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.
두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.
x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.

출력: 
각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 그래프에서의 최장 경로의 길이를 출력한다.

제한사항:

풀이: 
1st / 이어진 정점 개수 구하기
2nd / 경로 구하기

제출 이력:
1st / Fail, 이어진 정점이 아니라 경로를 구해야 함! 경로는 같은 정점의 번호가 2번 이상 등장할 수 없음!
2dn / Pass
'''

def dfs(i, cnt):
    global answer
    
    for j in range(1, N+1):
        if not visited[j] and graph[i][j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0
    else:
        if cnt > answer:
            answer = cnt
            
for tc in range(1, int(input())+1):
    answer = 0
    N, M = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    
    print("#{} {}".format(tc, answer))