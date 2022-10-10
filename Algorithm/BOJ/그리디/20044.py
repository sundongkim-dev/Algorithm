n = int(input())

li = list(map(int, input().split()))

li.sort()

answer = []
length = len(li)
for i in range(length//2):
    answer.append(li[i] + li[length-i-1])

print(min(answer))