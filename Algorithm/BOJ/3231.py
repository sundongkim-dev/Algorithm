n = int(input())

li = [[int(input()), i] for i in range(n)]
li.sort()

answer = 0

curidx = li[0][1]

for id, (value, idx) in enumerate(li):
    if id == 0:
        continue
    if curidx > idx:
        answer+=1
        
    curidx = idx

print(answer)