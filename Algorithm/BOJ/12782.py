import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    diff0, diff1 = 0, 0
    a, b = input().split()
    for i in range(len(a)):
        if a[i] != b[i]: # 각 자리 수가 다를 때
            if b[i] == '0': # 0 개수 세기
                diff0 += 1
            elif b[i] == '1': # 1 개수 세기
                diff1 += 1
    print(max(diff0, diff1)) # 0과 1 중 더 큰 값