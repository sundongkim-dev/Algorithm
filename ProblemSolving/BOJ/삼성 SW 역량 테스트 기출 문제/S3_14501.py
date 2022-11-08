'''
풀이 시작 시간: 2022-10-14 00:18
풀이 종료 시간: 2022-10-14 00:42

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
'''

'''
- dp활용해서 리스트 거꾸로 순회하여 풀이
Pass/1st
'''

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*N

if li[N-1][0] > 1:
    dp[N-1] = 0
else:
    dp[N-1] = li[N-1][1]

for idx in range(N-2, -1, -1):
    if li[idx][0]+idx < N:
        dp[idx] = max((li[idx][1] + dp[idx+li[idx][0]]), dp[idx+1])
    elif li[idx][0]+idx == N:
        dp[idx] = max(dp[idx+1], li[idx][1])
    else:
        dp[idx] = dp[idx+1]

print(dp[0])

