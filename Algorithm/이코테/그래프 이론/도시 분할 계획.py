'''
풀이 시작 시간: 2022-10-14 15:48
풀이 종료 시간: 2022-10-14 15:57

시간 제한 2초
메모리 제한 256MB

입력
첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. 
N은 2 이상 100,000 이하인 정수이고, M은 1 이상 1,000,000 이하인 정수이다.
그다음 줄부터 M줄에 걸쳐 길의 정보가 A,B,C 3개의 정수로 공백으로 구분되어 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C(1<=C<=1,000)라는 뜻이다.
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력
첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.
8
'''
'''
- 크루스칼 알고리즘을 활용하여 풀이
Pass/1st
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [x for x in range(N+1)]

roads = []
answer = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

roads.sort()
maxRoads = 0

for item in roads:
    cost, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        maxRoads = cost

print(answer - maxRoads)
 