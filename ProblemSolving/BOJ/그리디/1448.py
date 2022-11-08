import sys

input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

for idx in range(N-2):
    maxLen = li[idx]
    if li[idx] < li[idx+1] + li[idx+2]:
        print(li[idx]+li[idx+1]+li[idx+2])
        break
else:
    print(-1)