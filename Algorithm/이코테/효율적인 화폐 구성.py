'''
풀이 시작 시간: 2022-10-13 22:44
풀이 종료 시간: 2022-10-13 22:49

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 N, M이 주어진다. (1<=N<=100, 1<=M<=10,000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.
2 15
2
3

3 4
3
5
7

출력
첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1을 출력한다.
5

-1
'''

'''
- DP를 활용하여 풀이
Pass/1st
'''

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

dp = [10_001]*(M+1)
dp[0] = 0
for i in range(N):
    for j in range(money[i], M+1):
        if dp[j-money[i]] != 10001:
            dp[j] = min(dp[j], dp[j-money[i]]+1)

if dp[M] == 10_001:
    print(-1)
else:
    print(dp[M])


