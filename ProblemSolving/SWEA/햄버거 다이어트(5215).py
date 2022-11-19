'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 16:45
풀이 종료 시간: 2022-11-19 17:12

시간 제한: 20개/16초
메모리 제한: 256MB

입력: 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 
각 테스트 케이스의 첫 번째 줄에는 재료의 수, 제한 칼로리를 나타내는 N, L(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)가 공백으로 구분되어 주어진다.
다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는 Ti, Ki(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)가 공백으로 구분되어 주어진다.

출력: 
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력한다.

제한사항:

풀이: 
1st / 그리디로 구현
2nd / dfs로 구현
3rd / 조합으로 구현

제출 이력:
1st / Fail
2nd / Pass
3rd / Pass
'''
from itertools import combinations

def solution():
    global answer, info, N, L
    for idx in range(1, N+1):
        for combi in combinations(info, idx):
            kcal = 0
            score = 0
            for v in range(len(combi)):
                kcal += combi[v][1]
                score += combi[v][0]
            if kcal > L:
                continue
            if answer < score:
                answer = score

def dfs(idx, score, cal):
    global answer
    if cal > L:
        return
    if score > answer:
        answer = score
    if idx == N:
        return
    dfs(idx+1, score, cal)
    dfs(idx+1, score+info[idx][0], cal+info[idx][1])

for tc in range(1, int(input())+1):
    answer = 0
    N, L = map(int, input().split())
    info = []
    for i in range(N):
        t, k = map(int, input().split())
        info.append([t,k])
    
    #dfs(0,0,0)
    solution()
    
    print("#{} {}".format(tc, answer))