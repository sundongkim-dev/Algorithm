n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
answer = 0

for i in range(len(li)):
    if i<=1:
        answer += li[i]
    else:
        answer += li[0] + li[i]

print(answer)