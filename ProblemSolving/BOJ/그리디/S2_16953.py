'''
출처: https://www.acmicpc.net/problem/16953

풀이 시작 시간: 2022-12-09 19:54
풀이 종료 시간: 2022-12-09 20:07

시간 제한: 2초
메모리 제한: 512MB

입력: 
첫째 줄에 A, B (1 ≤ A < B ≤ 1e9)가 주어진다.

출력: 
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 
만들 수 없는 경우에는 -1을 출력한다.

제한사항: 

풀이: 
1st / 그리디 알고리즘 bottom-up
2nd / 그리디 알고리즘 top-down

제출 이력:
1st / Pass
'''

import sys
input = sys.stdin.readline

# A, B = map(int, input().split())
# answer = 0
# li = [A]
# flag = False
# while True:
#     answer += 1
#     if len(li) == 0:
#         break
#     tmp = []
#     for i in li:
#         if i > B:
#             continue            
#         tmp.append(i*2)
#         tmp.append(i*10+1)
#     if B in tmp:
#         flag = True
#         break
#     li = tmp.copy()
# if flag:
#     print(answer+1)
# else:
#     print(-1)

A, B = map(int, input().split())
answer = 1
while B != A:
    answer += 1
    tmp = B
    if B%10 == 1:
        B //= 10
    elif B%2 == 0:
        B //= 2
    if tmp == B:
        print(-1)
        break
else:
    print(answer)
    