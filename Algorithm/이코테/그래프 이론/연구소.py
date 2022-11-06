'''
출처: https://www.acmicpc.net/problem/14502

풀이 시작 시간: 2022-11-06 18:56
풀이 종료 시간: 2022-11-05 19:48

시간 제한: 2초
메모리 제한: 512MB

입력: 
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

출력: 
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

제한사항:

풀이: 
1st / 모든 경우의 수의 벽을 세우고 BFS로 바이러스를 전파한 후 안전한 공간 계산

제출 이력:
1st / Pass
'''

from itertools import combinations
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
virus = []
space = []

for i in range(N):
    lab.append([])
    line = list(map(int, input().split()))
    for j in range(len(line)):
        lab[i].append(line[j])
        if line[j] == 2:
            virus.append((i, j))
        elif line[j] == 0:
            space.append((i, j))

curSpace = len(space) - 3
maxSpace = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def changeLab(tmpLab, combi):
    for item in combi:
        a, b = item
        tmpLab[a][b] = 1
    return tmpLab

def bfs(tmp, virus, curSpace):
    global maxSpace, N, M
    while virus:
        x, y = virus.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus.append((nx, ny))
                curSpace -= 1

                if curSpace < maxSpace:
                    return maxSpace
                
    return curSpace


for combi in combinations(space, 3):
    tmpLab = copy.deepcopy(lab)
    tmpLab = changeLab(tmpLab, combi)

    maxSpace = max(bfs(tmpLab, virus.copy(), curSpace), maxSpace)

print(maxSpace)
