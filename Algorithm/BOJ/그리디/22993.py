import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

myAtk = li[0]
li.pop(0)

li.sort()

for idx in range(N-1):
    if myAtk > li[idx]:
        myAtk += li[idx]
    else:
        print("No")
        break
else:
    print("Yes")