import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    data = sorted([int(sys.stdin.readline()) for _ in range(n)])

    loc = 0
    flag = True
    for i in range(1, len(data)):
        interval = data[i] - data[i-1]
        if interval > 200:
            flag = False
            break
        loc += interval

    if loc < 1322:
        flag = False

    if flag:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')