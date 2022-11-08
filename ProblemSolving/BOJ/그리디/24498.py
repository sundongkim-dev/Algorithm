import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

height=[]

if N <= 2:
    print(max(li))
else:
    for i in range(1, N-1):
        ans= li[i]+min(li[i-1],li[i+1])
        height.append(ans)
        
    height.append(max(li[0],li[-1]))

    print(max(height))