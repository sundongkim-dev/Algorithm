N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)

answer = 0
for idx, item in enumerate(li, 1):
    val = (item - (idx-1))
    if val <= 0:
        continue
    answer += val 

print(answer)
