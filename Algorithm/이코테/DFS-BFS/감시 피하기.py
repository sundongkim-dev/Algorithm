'''
출처: https://www.acmicpc.net/problem/18428

풀이 시작 시간: 2022-11-08 13:41
풀이 종료 시간: 2022-11-08 14:27

시간 제한: 2초
메모리 제한: 256MB

입력: 
첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6) 
둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 
각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. 
해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.

출력: 
첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다. 
모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.

제한사항:

풀이: 
1st / 장애물을 설치하는 모든 경우의 수에 대해서 모든 선생님들을 검사해서 결과를 얻는다. 31*30*29/6만큼의 연산량을 가진다.

제출 이력: 
1st / Pass
'''

from collections import deque
from itertools import combinations
import copy

# 상하좌우
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

classroom = []
student = []
teacher = []
blank = []

N = int(input())
for i in range(N):
    line = list(input().split())
    classroom.append(line)
    for idx, j in enumerate(line):
        if j == 'X':
            blank.append((i,idx))
        elif j == 'S':
            student.append((i,idx))
        elif j == 'T':
            teacher.append((i,idx))

def calc(pos, dir):
    flag = False
    q = deque([pos])
    while q:
        a, b = q.popleft()
        
        nx = a + dx[dir]
        ny = b + dy[dir]
        if 0<=nx<N and 0<=ny<N:
            if tmpClassroom[nx][ny] == 'X' or tmpClassroom[nx][ny] == 'T':
                q.append([nx,ny])
            elif tmpClassroom[nx][ny] == 'S':
                flag = True
                break
            elif tmpClassroom[nx][ny] == 'O':
                break
    return flag

answerFlag = False
# 가능한 모든 장애물의 조합
for combi in combinations(blank, 3):
    # 사본에 장애물 설치
    tmpClassroom = copy.deepcopy(classroom)
    for item in combi:
        a, b = item
        tmpClassroom[a][b] = 'O'
    # 모든 선생님들 기준에서 검사
    chk = []
    for pos in teacher:
        # 상
        flag1 = calc(pos, 0)
        if flag1: # 선생님 경로에 학생들 있음
            chk.append("false")
            break
        # 하            
        flag2 = calc(pos, 1)
        if flag2:
            chk.append("false")
            break
        # 좌
        flag3 = calc(pos, 2)
        if flag3:
            chk.append("false")
            break
        # 우
        flag4 = calc(pos, 3)
        if flag4:
            chk.append("false")
            break
        chk.append("true")
    
    # 모든 선생님들이 true라면 가능한 경우
    if "false" not in chk:
        answerFlag = True
        break


if answerFlag == True:
    answer = "YES"
else:
    answer = "NO"

print(answer)