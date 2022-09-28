n = int(input())

answer = 0
dp = [0 for  i in range(5001)]
dp[0] = -1; dp[1] = -1; dp[2] = -1; dp[3] = 1; dp[4] = -1; dp[5] = 1; dp[6] = 2

for i in range(7, 5001):
    if dp[i-3] == -1:
        if dp[i-5] == -1:
            dp[i] = -1
        else:
            dp[i] = dp[i-5]+1
    elif dp[i-5] == -1:
        if dp[i-3] == -1:
            dp[i] = -1
        else:
            dp[i] = dp[i-3]+1
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[n])