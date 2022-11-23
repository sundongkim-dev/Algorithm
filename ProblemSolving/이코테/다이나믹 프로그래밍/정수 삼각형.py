'''
출처: https://www.acmicpc.net/problem/1932

풀이 시작 시간: 2022-11-24 08:14
풀이 종료 시간: 2022-11-24 08:21

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력: 
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

제한사항: 

풀이: 
1st / dp로 구현

제출 이력:
1st / Pass
'''

n = int(input())
arr = [[0]*n for _ in range(n)]
for i in range(n):
    li = list(map(int, input().split()))
    for idx, j in enumerate(li):
        arr[i][idx] = j

for i in range(1, n):
    for j in range(n):
        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))