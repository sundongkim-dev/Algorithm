import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    # 상어가 공간에 들어가면 (0,0)에 있는 물고리를 먹고 방향을 취한다. 번호 더해주기.
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    # 번호 먹으면 0으로 바꿔줌
    board[sx][sy][0] = 0
    
    # 물고기 이동
    for idx in range(1, 17):
        x, y = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == idx:
                    x, y = i, j
                    break
            if x != -1 and y != -1:
                break
        if x == -1 and y == -1:
            continue
        dir = board[i][j][1]

        for i in range(8):
            nd = (dir+i)%8
            nx, ny = x+dx[nd], y+dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[x][y][1] = nd
            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            break
    
    # 상어가 이동
    sd = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[sd] * i
        ny = sy + dy[sd] * i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)