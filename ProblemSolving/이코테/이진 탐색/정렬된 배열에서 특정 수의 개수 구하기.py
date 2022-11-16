'''
출처: Zoho 인터뷰

풀이 시작 시간: 2022-11-16 9:45
풀이 종료 시간: 2022-11-16 9:48

시간 제한: 
메모리 제한: 

입력: 

출력: 

제한사항: O(logN)으로 풀어야 한다.

풀이: 이분탐색으로 푼다.

제출 이력:

'''
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
num = list(map(int, input().split()))

left = bisect_left(num, x)
right = bisect_right(num, x)
result = left - right

if result == 0:
    print(-1)
else:
    print(result)
