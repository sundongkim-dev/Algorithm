'''
출처: Flipkart 인터뷰

풀이 시작 시간: 2022-11-23 19:55
풀이 종료 시간: 2022-11-23 20:04

시간 제한: 1초
메모리 제한: 128MB

입력: 
첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20) 
둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)

출력: 
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다. 각 테스트 케이스는 줄 바꿈을 이요해 구분합니다.

제한사항: 

풀이: 
1st / dp로 구현

제출 이력:
1st / Pass
'''

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m-1])
    print(answer)