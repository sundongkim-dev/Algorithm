T = int(input())

for i in range(T):
    N = int(input())
    li = list(input().split())
    
    tmp = []
    for item in li:
        if len(tmp) == 0:
            tmp.append(item)
        else:
            if item <= tmp[0]:
                tmp.insert(0, item)
            else:
                tmp.append(item)
    print(''.join(tmp))
