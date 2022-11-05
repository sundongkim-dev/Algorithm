'''
출처: https://www.acmicpc.net/problem/18352

풀이 시작 시간: 2022-11-05 21:58
풀이 종료 시간: 2022-11-05 22:29

시간 제한: 2초
메모리 제한: 256MB

입력: 
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

출력: 
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

제한사항:

풀이: 
1st / BFS로 모든 점의 거리를 계산 후 만족하는 점들만 출력해주면 된다.

제출 이력:
1st / Pass
'''
from collections import deque
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph =[[] for _ in range(N+1)]
distance = [-1]*(N+1)
distance[X] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
q = deque([X])
while q:
    val = q.popleft()
    for i in graph[val]:
        if distance[i] == -1:
            distance[i] = distance[val] + 1
            q.append(i)

chk = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        chk = True

if chk == False:
    print(-1)