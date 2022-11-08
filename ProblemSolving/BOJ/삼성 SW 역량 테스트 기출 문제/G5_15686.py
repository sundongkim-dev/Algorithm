'''
풀이 시작 시간: 2022-10-14 20:12
풀이 종료 시간: 2022-10-14 20:

시간 제한 1초
메모리 제한 512MB

입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
'''

'''
- 치킨집 조합을 이용하여 완전탐색
Pass/1st
'''

from itertools import combinations

N, M = map(int, input().split())
cityInfo  = [list(map(int, input().split())) for _ in range(N)]

house = []
kfc = []

for i in range(N):
    for j in range(N):
        if cityInfo[i][j] == 2:
            kfc.append([i+1,j+1])
        elif cityInfo[i][j] == 1:
            house.append([i+1,j+1])

def getDist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

answer = []
for item in combinations(kfc, r=M):
    tmp = []
    for home in house:
        val = 987654321
        # 각 집마다 정해진 치긴 가게에 대해 모든 거리 구하고 그 중 최소 거리만 취함
        for i in item:
            val = min(val, getDist(i, home))
        tmp.append(val)
    answer.append(sum(tmp))

print(min(answer))       