'''
풀이 시작 시간: 2022-10-14 15:58
풀이 종료 시간: 2022-10-14 16:

시간 제한 2초
메모리 제한 128MB

입력
첫째 줄에 동빈이가 듣고자 하는 강의의 수 N(1<=N<=500)이 주어진다.
다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분한다.
이때 강의 시간은 100,000 이하의 자연수이다.
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

출력
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.
10
20
14
18
17
'''
'''
- 위상 정렬 알고리즘을 활용하여 풀이
Pass/1st
'''

from collections import deque
import copy


N = int(input())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
time = [0]*(N+1)

for i in range(1, N+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    for prerequisite in line[1:-1]:
        indegree[i] += 1
        graph[prerequisite].append(i)

answer = copy.deepcopy(time)
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    val = q.popleft()
    for i in graph[val]:
        answer[i] = max(answer[i], answer[val] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(answer[i])
