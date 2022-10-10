import sys

input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))

dp = [0 for i in range(N)]
dp[0] = 0

minNum = li[0]
print(dp[0])
for idx in range(1, N):
    minNum = min(minNum, li[idx])
    dp[idx] = max(dp[idx-1], li[idx] - minNum)
    print(dp[idx])