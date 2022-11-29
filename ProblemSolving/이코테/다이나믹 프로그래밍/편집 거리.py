'''
출처: Goldman Sachs 인터뷰

풀이 시작 시간: 2022-11-25 12:37
풀이 종료 시간: 2022-11-25 12:54

시간 제한: 1초
메모리 제한: 128MB

입력: 
두 문자열 A와 B가 한 줄에 하나씩 주어집니다.
각 문자열은 영문 알파벳으로만 구성되어 있으며, 각 문자열의 길이는 1보다 크거나 같고, 5,000보다 작거나 같습니다.

출력: 
최소 편집 거리를 출력합니다.

제한사항: 

풀이: 
1st / dp로 구현

제출 이력:
1st / Pass
'''

a = input()
b = input()

n = len(a)
m = len(b)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j

for i in range(1, n+1):
    for j in range(m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

print(dp[n][m])