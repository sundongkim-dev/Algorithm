'''
출처: https://www.acmicpc.net/problem/15686

풀이 시작 시간: 2022-11-04 17:32
풀이 종료 시간: 2022-11-04 18:11

시간 제한: 1초
메모리 제한: 512MB

입력: 
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력: 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

제한사항:

풀이: 
1st / 모든 가능한 치킨 집의 경우의 수에 대해 모두 조사한다.

제출 이력:
1st / Pass
'''

from itertools import combinations

def getChickenDist(a, b, x, y):
    return abs(a-x) + abs(b-y)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chickenStation = []
home = []
answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chickenStation.append((i, j))

for item in combinations(chickenStation, r=M):
    tmp = []
    for a, b in home:
        val = 101
        for x, y in item:
            val = min(val, getChickenDist(x,y,a,b))
        tmp.append(val)
    answer.append(sum(tmp))

print(min(answer))