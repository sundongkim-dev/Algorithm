N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

answer = 0
for idx, item in enumerate(li):
    if idx > 0 and idx%3 == 2:
        continue
    else:
        answer += item

print(answer)

