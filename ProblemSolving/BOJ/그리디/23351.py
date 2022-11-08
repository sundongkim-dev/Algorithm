N, K, A, B = map(int, input().split())

answer = 1
li = [K]*N

idx = 0
while True:
    for i in range(A):
        li[idx] += B
        idx += 1
        if idx > N-1:
            idx = 0
    for i in range(N):
        li[i] -= 1
    if min(li) == 0:
        break 
    answer += 1

print(answer)