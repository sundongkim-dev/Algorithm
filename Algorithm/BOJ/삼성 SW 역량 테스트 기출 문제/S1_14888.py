'''
풀이 시작 시간: 2022-10-14 01:21
풀이 종료 시간: 2022-10-14 02:02

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
'''

'''
- itertools permutations를 활용해서 완전탐색
Fail/1st
- 시간 초과, 중복해서 탐색했기에 중복 제거 -> set 이용
Pass/2nd
'''

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())) # + - * /

sign = ['+', '-', '*', '/']
li = []
for idx, item in enumerate(B):
    li += sign[idx]*item

maxNum = -1_000_000_001
minNum = 1_000_000_001

s = set()
for item in permutations(li):
    pm = "".join(list(item))
    if pm in s:
        continue
    else:
        s.add(pm)
        num = A[0]
        for idx in range(N-1):
            val = A[idx+1]
            if item[idx] == '+':
                num += val
            elif item[idx] == '-':
                num -= val
            elif item[idx] == '*':
                num *= val
            elif item[idx] == '/':
                if num < 0:
                    num = abs(num)
                    num = num // val
                    num = -num
                else:
                    num = num // val
        maxNum = max(maxNum, num)
        minNum = min(minNum, num)

print(maxNum)
print(minNum)