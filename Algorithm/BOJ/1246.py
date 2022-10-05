N, M = map(int, input().split())

customer = []
for _ in range(M):
    customer.append(int(input()))

customer.sort()
length = len(customer)

answer = targetval = 0
for idx, i in enumerate(customer):
    num = min(N, length-idx)
    val = i*num
    if answer < val:
        targetval = i
        answer = val

print(targetval, answer)
