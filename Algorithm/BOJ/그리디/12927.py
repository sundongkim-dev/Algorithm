s = list(input())

ssize = len(s)
answer = 0
for idx, i in enumerate(s, 1):
    if i == 'Y':
        answer += 1
        curIdx = idx-1
        while curIdx < ssize:
            s[curIdx] = 'Y' if s[curIdx] == 'N' else 'N'
            curIdx += idx
    else:
        continue    

print(answer)