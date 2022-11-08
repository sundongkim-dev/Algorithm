def coupon(c):
    budget = B - (li[c][0] // 2 + li[c][1])
    total = 1

    if budget < 0:
        return 0
    for i in range(N):
        if li[i][0] + li[i][1] <= budget and i != c:
            budget -= (li[i][0] + li[i][1])
            total += 1
    return total

N, B = map(int, input().split())

li = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    li.append(tmp)

li.sort(key = lambda x : (x[0] + x[1]))

answer = 0

for i in range(N):
    if coupon(i) > answer:
        answer = coupon(i)

print(answer)