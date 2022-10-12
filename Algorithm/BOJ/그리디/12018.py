n, m = map(int, input().split())

subjects = []
minM = []

for _ in range(n):
    p, l = map(int, input().split())
    subject = list(map(int, input().split()))
    subject.sort(reverse=True)

    if p < l:
        minM.append(1)
    else:
        minM.append(subject[l-1])

minM.sort()
answer = 0; curM = 0
for i in minM:
    if curM+i > m:
        break
    curM += i
    answer += 1

print(answer)

