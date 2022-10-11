for _ in range(int(input())):
    n = int(input())
    target = list(map(int, input().split()))

    total = 0
    for i in range(1, n + 1):
        index = target.index(i)
        total += index
        del target[index]

    print(total)