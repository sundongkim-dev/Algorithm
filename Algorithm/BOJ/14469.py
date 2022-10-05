N = int(input())

li = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    li.append(tmp)

li.sort(key=lambda x : (x[0], x[1]))

ans = 0
for i in li:
    if ans < i[0]:
        ans = i[0]+i[1]
    else:
        ans += i[1]
        
print(ans)
