N = int(input())
li = list(map(int, input().split()))
li.sort()

last = 0
if len(li)%2 == 1:
    last = li.pop(-1)

answer = [li[i] + li[-i-1] for i in range(len(li)//2)]
answer.append(last)

print(max(answer))