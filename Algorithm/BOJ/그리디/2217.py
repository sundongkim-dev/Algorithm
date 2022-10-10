import sys

input=sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

answer = 0
for i in range(N):
    answer = max(answer, li[i]*(i+1))

print(answer)