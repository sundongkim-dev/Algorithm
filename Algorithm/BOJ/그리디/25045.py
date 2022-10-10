N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

idx = min(len(A), len(B))
answer = 0
for i in range(idx):
    
    if A[i] - B[i] > 0:
        answer += A[i]-B[i]
    else:
        break

print(answer)

