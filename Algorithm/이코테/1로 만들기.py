'''
풀이 시작 시간: 2022-10-13 22:20
풀이 종료 시간: 2022-10-13 22:31

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 정수 X가 주어진다.(1<=X<=30,000)
26

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
3
'''

'''
- 그리디하게 풀이
Fail/1st
- DP를 활용하여 풀이
Pass/1st
'''

X = int(input())
answer = 0

dp = [0]*(X+1)
dp[2] = 1; dp[3] = 1; dp[4] = 2; dp[5] = 1;

for i in range(6, X+1):
    tmp = []
    if i%5 == 0:
        tmp.append(dp[i//5])
    if i%3 == 0:
        tmp.append(dp[i//3])
    if i%2 == 0:
        tmp.append(dp[i//2])
    if len(tmp):
        dp[i] = min(dp[i-1], min(tmp)) + 1
    else:
        dp[i] = dp[i-1]+1

print(dp[X])