'''
출처: https://www.acmicpc.net/problem/14888

풀이 시작 시간: 2022-11-08 13:13
풀이 종료 시간: 2022-11-08 13:38

시간 제한: 2초
메모리 제한: 512MB

입력: 
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력: 
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

제한사항:

풀이: 
1st / 주어진 연산자들의 모든 순열을 구하고 연산해서 최댓값과 최솟값 구한다. 11!이 최대 가짓수
2nd / set을 만들어서 추가해서 이미 검사한 조합에 대해서는 skip

제출 이력: 
1st / 시간 초과
2nd / Pass
'''

from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
ops = ['+']*a + ['-']*b + ['*']*c + ['/']*d

s = set()
maxNum = -1e9-1
minNum = 1e9+1
for combi in permutations(ops, N-1):
    pm = "".join(list(combi))
    if pm in s:
        continue
    else:
        s.add(pm)
    tmp = num[0]
    for idx in range(1, N):
        if combi[idx-1] == '+':
            tmp += num[idx]
        elif combi[idx-1] == '-':
            tmp -= num[idx]
        elif combi[idx-1] == '*':
            tmp *= num[idx]
        elif combi[idx-1] == '/':
            if tmp < 0 and num[idx] > 0:
                tmp = -((-tmp)//num[idx])
            else: 
                tmp //= num[idx]

    maxNum = max(maxNum, tmp)
    minNum = min(minNum, tmp)

print(maxNum)
print(minNum)





