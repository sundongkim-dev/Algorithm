'''
풀이 시작 시간: 2022-10-14 00:51
풀이 종료 시간: 2022-10-14 01:10

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 
둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. 
Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''

'''
- itertools combinations를 활용해서 완전탐색
Pass/1st
'''
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

li = [x for x in range(N)]
answer = 987654321

for item in combinations(li, r=N//2):
    scoreA = scoreB = 0
    teamA = list(item)
    teamB = [x for x in li if x not in item]
    
    
    for i in combinations(teamA, r=2):
        i, j = list(i)
        scoreA += S[i][j] + S[j][i]

    for i in combinations(teamB, r=2):
        i, j = list(i)
        scoreB += S[i][j] + S[j][i]
    
    answer = min(answer, abs(scoreA-scoreB))

print(answer)
