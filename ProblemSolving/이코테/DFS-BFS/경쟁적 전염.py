'''
출처: https://www.acmicpc.net/problem/18405

풀이 시작 시간: 2022-11-07 16:32
풀이 종료 시간: 2022-11-07 17:13

시간 제한: 1초
메모리 제한: 256MB

입력: 
첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 
둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 
각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 
단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. 
N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

출력: 
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

제한사항:

풀이: 
1st / BFS로 값이 작은 바이러스부터 퍼뜨린다.

제출 이력:
1st / Pass
'''
from collections import deque

lab = []
N, K = map(int, input().split())
virus = [[] for _ in range(K+1)]


for i in range(N):
    lab.append([])
    line = list(map(int, input().split()))
    for j in range(len(line)):
        lab[i].append(line[j])
        if line[j] != 0:
            virus[line[j]].append((i, j))

S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
for i in range(1, K+1):
    if virus[i]:
        for item in virus[i]:
            data = (i, item, 0)
            q.append(data)

while q:
    val, (x,y), second = q.popleft()
    if second == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and lab[nx][ny] == 0:
            lab[nx][ny] = val
            data = (val, (nx, ny), second+1)
            q.append(data)
            
print(lab[X-1][Y-1])
    