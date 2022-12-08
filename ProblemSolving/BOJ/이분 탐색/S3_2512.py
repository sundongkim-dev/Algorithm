'''
출처: https://www.acmicpc.net/problem/2512

풀이 시작 시간: 2022-12-02 09:53
풀이 종료 시간: 2022-12-02 10:08

시간 제한: 5초
메모리 제한: 128MB

입력: 
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 
다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 
이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. 
M은 N 이상 1,000,000,000 이하이다. 

출력: 
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 

제한사항: 

풀이: 
1st / 이분 탐색, 파라메트릭 서치

제출 이력:
1st / Pass
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
money = int(input())
low, high = 0, max(arr)

while low <= high:
    mid = (low+high) // 2
    tmp = 0
    for i in arr:
        if i >= mid:
            tmp += mid
        else:
            tmp += i
    if tmp <= money:
        low = mid+1
    else:
        high = mid-1
        
print(high)