N = int(input())

li = []

for i in range(N):
    abpair = list(map(int, input().split()))
    li.append(abpair)

li.sort()

answer = 0
for i in range(1, N+1):
    answer += (li[i-1][0]*i + li[i-1][1])

print(answer)
