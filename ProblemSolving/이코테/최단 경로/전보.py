'''
풀이 시작 시간: 2022-10-14 15:08
풀이 종료 시간: 2022-10-14 15:16

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
(1<=N<=30,000, 1<=M<=200,000, 1<=C<=N)
둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다.
이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다.
(1<=X,Y<=N, 1<=Z<=1,000)
3 2 1
1 2 4
1 3 2

출력
첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백하여 구분하여 출력한다.
2 4
'''
'''
- 다익스트라 알고리즘을 활용하여 풀이
Pass/1st
'''

import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

answer = 0
time_elapsed = 0
for item in distance:
    if item != INF:
        answer += 1
        time_elapsed = max(time_elapsed, item)

print(answer-1, time_elapsed)
