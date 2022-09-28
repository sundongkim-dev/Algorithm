n = int(input())
li = list(map(int, input().split()))

li.sort()

answer = 0
tmp = 0
for i in li:
    tmp += i
    answer += tmp

print(answer)

