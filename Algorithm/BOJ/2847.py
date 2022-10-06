N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

answer = 0
for idx in range(N-1, 0, -1):
    while li[idx] <= li[idx-1]:
        li[idx-1] -= 1
        answer += 1

print(answer)