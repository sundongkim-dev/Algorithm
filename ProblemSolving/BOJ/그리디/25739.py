import sys

input = sys.stdin.readline

N = int(input())

ali = list(map(int, input().split()))

tmp = [0]*2
ans = [0,0]

for i in range(N):
    x = ali[i] % 2
    tmp[x] += 1
    ans[x] += tmp[1-x]

print(min(ans))