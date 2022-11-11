'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60063

풀이 시작 시간: 2022-11-10 20:54
풀이 종료 시간: 2022-11-10 23:27

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:
board의 한 변의 길이는 5 이상 100 이하입니다.
board의 원소는 0 또는 1입니다.
로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

입출력 예시:
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = 7
	

풀이: 
1st / bfs로 탐색한다.

제출 이력:
1st / Pass
'''

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 가로
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    # 세로      
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next_pos              

def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)] # 외곽에 벽 세워주기
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    q = deque()
    visited = []
    pos = {(1,1), (1,2)} # 시작 위치
    q.append((pos, 0))
    visited.append(pos)
    
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    
    return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = solution(board)
print(result)