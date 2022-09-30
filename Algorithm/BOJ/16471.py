N = int(input())

juli = list(map(int, input().split()))
sali = list(map(int, input().split()))

juli.sort()
sali.sort()

idx = 0
count = 0

for item in juli:
    while idx < N:
        if sali[idx] > item:
            idx += 1
            count += 1
            break
        else:
            idx += 1

if count >= (N+1)/2:
    print("YES")
else:
    print("NO")