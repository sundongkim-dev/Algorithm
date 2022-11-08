'''
출처: https://www.acmicpc.net/problem/3190

풀이 시작 시간: 2022-11-03 20:03
풀이 종료 시간: 2022-11-03 20:56

시간 제한: 1초
메모리 제한: 128MB

입력: 
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력: 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

제한사항:
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

풀이: 
1st / 차례대로 구현한다.

제출 이력:
1st / Pass
'''

N = int(input())
K = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
cmd = []

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1
graph[1][1] = 2


L = int(input())
for _ in range(L):
    X, C = input().split()
    cmd.append((int(X), C))
dir_dict = {'D': 1, 'L': -1}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0
r, c = 1, 1 # 뱀의 머리 위치
length = 1 # 뱀의 길이
idx = 0
dir = 0
q = [(r, c)]

def rotate(dir, C):
    if C == 'L':
        dir = (dir-1)%4
    else:
        dir = (dir+1)%4
    return dir

while True:
    # step 1. 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
    nx = r + dx[dir]
    ny = c + dy[dir]
    
    if 1<=nx<=N and 1<=ny<=N and graph[nx][ny] != 2:
        # step 2. 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸길이는 변하지 않습니다.
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            graph[px][py] = 0
        # step 2. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            q.append((nx, ny))
    else:
        answer += 1
        break
    
    r, c = nx, ny  
    answer += 1
    # [Optional] step 3. 방향 전환하기    
    if idx < L and answer == cmd[idx][0]:
        dir = rotate(dir, cmd[idx][1])
        idx+=1

print(answer)
    
    
    
   
    
    
    
    


