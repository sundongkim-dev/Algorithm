import sys

input = sys.stdin.readline

N, K = map(int, input().split())

li = []
for _ in range(N):
    li.append(int(input()))

answer = 0
idx = N-1
while K>0:
    if K // li[idx] > 0:
        answer += (K//li[idx])
        K %= li[idx]
    else:
        idx -= 1

print(answer)