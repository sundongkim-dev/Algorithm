N, L = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
tmp = li[0]

answer = 1
for i in range(len(li)):
    if tmp + L > li[i]:
        pass
    else:
        answer += 1
        tmp = li[i]
        
print(answer)
