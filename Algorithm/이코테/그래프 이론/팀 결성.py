'''
풀이 시작 시간: 2022-10-14 15:31
풀이 종료 시간: 2022-10-14 15:40

시간 제한 2초
메모리 제한 128MB

입력
첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.(1<=N,M<=100,000)
다음 M개의 줄에는 각각의 연산이 주어진다.
'팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
'같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는 지를 확인하는 연산이다.
a와 b는 N 이하의 양의 정수이다.
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
NO
NO
YES
'''
'''
- union-find 알고리즘을 활용하여 풀이
Pass/1st
'''
def find_team(parent, x):
    # 자기 자신이 부모가 아니면, 탐색
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]

def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [x for x in range(N+1)]

for _ in range(M):
    cmd, a, b = map(int, input().split())
    # 팀 합치기
    if cmd == 0:
        union_team(parent, a, b)
    # 같은 팀 여부 확인
    elif cmd == 1:
        if find_team(parent, a) == find_team(parent, b):
            print("YES")
        else:
            print("NO")