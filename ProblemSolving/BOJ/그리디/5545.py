N = int(input())

A, B = map(int, input().split())
C = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)
cost = A

curCalc = C
answer = [curCalc//cost]

for i in range(N):
    tmp = li[:i+1]
    cost += B*len(tmp)
    for item in tmp:
        curCalc += item
    answer.append(curCalc//cost)
    cost = A
    curCalc = C

print(max(answer))
