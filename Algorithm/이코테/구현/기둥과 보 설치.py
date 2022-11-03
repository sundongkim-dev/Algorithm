'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60061

풀이 시작 시간: 2022-11-03 20:57
풀이 종료 시간: 2022-11-03 19:47

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:
n은 5 이상 100 이하인 자연수입니다.
build_frame의 세로(행) 길이는 1 이상 1,000 이하입니다.
build_frame의 가로(열) 길이는 4입니다.
build_frame의 원소는 [x, y, a, b]형태입니다.
x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
바닥에 보를 설치 하는 경우는 없습니다.
구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.
return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
return 하는 배열의 원소는 [x, y, a] 형식입니다.
x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

입출력 예시:
n = 5	
build_frame	= [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

풀이: 
1st / 완전탐색으로 다 대입해본다.

제출 이력:
1st / Pass
'''


def possible(graph):
    for x, y, a in graph:
        # 기둥
        if a == 0:
            if y == 0 or [x-1, y, 1] in graph or [x, y, 1] in graph or [x, y-1, 0] in graph:
                continue
            return False
        # 보
        elif a == 1:
            if [x, y-1, 0] in graph or [x+1, y-1, 0] in graph or ([x-1, y, 1] in graph and [x+1, y, 1] in graph):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 삭제하는 경우:
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
    return sorted(answer)


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
result = solution(n, build_frame)
print(result)
