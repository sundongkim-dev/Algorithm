'''
출처: https://www.acmicpc.net/problem/18353

풀이 시작 시간: 2022-11-25 12:19
풀이 종료 시간: 2022-11-25 12:27

시간 제한: 1초
메모리 제한: 128MB

입력: 
첫째 줄에 n이 입력된다.(1 <= n <= 1,000)

출력: 
n번째 못생긴 수를 출력한다.

제한사항: 

풀이: 
1st / dp로 구현

제출 이력:
1st / Pass
'''

n = int(input())
dp = [0]*n
dp[0] = 1

i2=i3=i5=0
n2,n3,n5 = 2,3,5

for i in range(1, n):
    dp[i] = min(n2,n3,n5)
    if dp[i] == n2:
        i2 += 1
        n2 = dp[i2] * 2
    if dp[i] == n3:
        i3 += 1
        n3 = dp[i3] * 3
    if dp[i] == n5:
        i5 += 1
        n5 = dp[i5] * 5
    print(dp)