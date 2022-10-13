'''
풀이 시작 시간: 2022-10-14 00:02
풀이 종료 시간: 2022-10-14 00:12

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.
셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)

출력
각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력한다.
'''

'''
- 그리디하게 풀이
Fail/1st
- 나머지 연산: 음수일 때, 0으로 바꿔주는 처리해주어야 함
Pass/2nd
'''

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def minusAdmin(a):
    global B
    if a-B < 0:
        return 0
    return a-B

A = list(map(minusAdmin, A))
answer = N

for item in A:
    if item%C == 0:
        answer += (item//C)
    else:
        answer += (item//C) + 1

print(answer)