'''
풀이 시작 시간: 2022-10-15 11:48
풀이 종료 시간: 2022-10-15 12:22

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
'''

'''
- dfs 활용해서 시뮬레이션 반복
Pass/1st
'''
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
move = [(0,1), (1,0), (-1,0)]
answer = 0
maxNum = max(map(max, arr))

def dfs(x, y, cnt, num):
    global answer
    if not cnt:
        answer = max(answer, num)
        return
    if answer >= num + cnt*maxNum:
        return
    
    for a,b in move:
        dx, dy = x+a, y+b
        if 0<=dx<n and 0<=dy<m:
            if not visited[dx][dy]:
                visited[dx][dy] = 1
                if cnt == 2:
                    # ㅗ 모양
                    dfs(x, y, cnt-1, num+arr[dx][dy])
                dfs(dx, dy, cnt-1, num+arr[dx][dy])
                visited[dx][dy] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 3, arr[i][j])
        visited[i][j] = 0

print(answer)     