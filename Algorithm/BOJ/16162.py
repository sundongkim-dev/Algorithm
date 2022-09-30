N, A, D = map(int, input().split())

li = list(map(int, input().split()))

cur = A

answer = 0
for item in li:
    if item == cur:
        cur += D
        answer += 1
    else:
        pass

print(answer)