'''
출처: https://www.acmicpc.net/problem/2263

풀이 시작 시간: 2022-11-30 09:58
풀이 종료 시간: 2022-11-30 10:26

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 
다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 
이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

출력: 
1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)

제한사항: 

풀이: 
1st / union-find 활용
2nd / Recursion depth 늘리기

제출 이력:
1st / Fail
2nd / Pass
'''

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)