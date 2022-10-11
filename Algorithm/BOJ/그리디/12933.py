s = input()
visited = [False]*len(s)
answer = 0

if len(s)%5 != 0:
    print(-1)
else:
    slen = len(s)
    for i in range(slen):
        if s[i] == 'q' and not visited[i]:
            quack = "quack"
            j=0; first=True
            for idx in range(i, slen):
                if s[idx] == quack[j] and not visited[idx]:
                    visited[idx] = True
                    if s[idx] == 'k':
                        if first:
                            answer += 1
                            first = False
                        j = 0
                        continue
                    j+=1

    if not all(visited) or answer == 0:
        print(-1)
    else:
        print(answer)