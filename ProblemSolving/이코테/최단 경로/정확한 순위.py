'''
출처: K 대회

풀이 시작 시간: 2022-11-27 10:31
풀이 종료 시간: 2022-11-26 10:44

시간 제한: 5초
메모리 제한: 128MB

입력: 
첫째 줄에 학생들의 수 N(2 <= N <= 500)과 두 학생의 성적을 비교한 횟수 M(2 <= M <= 10,000)이 주어집니다.
다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A, B가 주어집니다. 이는 A번 학생의 성적이 B번 학생보다 낮다는 것을 의미합니다.

출력: 
첫째 줄에 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력합니다.

제한사항: 

풀이: 
1st / 플로이드 워셜

제출 이력:
1st / Pass
'''

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt +=  1
    if cnt == n:
        answer += 1
print(answer)