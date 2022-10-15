'''
풀이 시작 시간: 2022-10-15 11:44
풀이 종료 시간: 2022-10-15 11:59

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 
그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.
둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 
주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

출력
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 
만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
'''

'''
- 주사위 각 operation마다 움직임 전부 세팅
Pass/2nd
'''
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0]*6

def roll(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    # 서
    elif dir == 2: 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    # 북
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    # 남
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y
for oper in cmd:
    nx += dx[oper-1]
    ny += dy[oper-1]

    if nx<0 or ny<0 or nx>=n or ny>=m:
        nx -= dx[oper-1]
        ny -= dy[oper-1]
        continue
    
    roll(oper)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0

    print(dice[0])

