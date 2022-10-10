li = []
N = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(N) > 0:
        if num[0] == N[0]:
            N = N[1:]
        num = num[1:]
    if N == '':
        print(i)
        break