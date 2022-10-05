from collections import Counter
T = int(input())

for _ in range(T):
    answer = 0
    a, b = map(str, input().split())
    #ali = list(a)
    #bli = list(b)
    acounter = Counter(a)
    bcounter = Counter(b)
    # 개수가 일치하는 지 확인
    zeroflag = True if acounter['0'] == bcounter['0'] else False
    oneflag = True if acounter['1'] == bcounter['1'] else False
    # 일치하면 위치만 바꿔주면 되고 
    if zeroflag is True and oneflag is True:
        pos = 0
        for c1, c2 in zip(a, b):
            if c1 is not c2:
                pos += 1
        answr = pos // 2
    # 불일치하면 그만큼 바꾸고 위치 바꾸기
    else:
        val = min(acounter.values())
    print(answer)