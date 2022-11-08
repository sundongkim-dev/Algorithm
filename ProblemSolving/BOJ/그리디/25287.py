T = int(input())

for test_case in range(T):
    li = []
    cost = 0
    while True:
        L = int(input())
        if L == 0:
            break
        li.append(L)
    
    li.sort(reverse=True)
    n = 1
    for item in li:
        cost += (2 * (item**n))
        n += 1
        if cost > 5*(10**6):
            print("Too expensive")
            break
    else:
        print(cost)

