T = int(input())

for _ in range(T):
    N = int(input())
    startState = list(input())
    endState = list(input())
    
    diff1 = diff2 = 0
    for a, b in zip(startState, endState):
        if a == 'W' and a != b:
            diff1 += 1
        elif a == 'B' and a != b:
            diff2 += 1
        else:
            pass
    print(max(diff1, diff2))


