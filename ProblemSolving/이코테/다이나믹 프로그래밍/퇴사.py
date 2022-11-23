'''
출처: https://www.acmicpc.net/problem/14501

풀이 시작 시간: 2022-11-24 08:31
풀이 종료 시간: 2022-11-24 08:51

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력: 
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

제한사항: 

풀이: 
1st / dp로 구현

제출 이력:
1st / Pass
'''

n = int(input())
info = []
for i in range(n):
    info.append(list(map(int, input().split())))

dp = [0]*(n+1)
answer = 0
for i in range(n-1, -1, -1):
    t = info[i][0] + i
    if t <= n:
        dp[i] = max(info[i][1] + dp[t], answer)
        answer = dp[i]
    else:
        dp[i] = answer
print(answer)