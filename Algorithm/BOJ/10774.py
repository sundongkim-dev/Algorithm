import sys

input = sys.stdin.readline
sizedict = {"L": 3, "M": 2, "S": 1}

n = int(input())
Q = int(input())

size = [sizedict[input().rstrip()] for i in range(n)]
req = [4]*n

for i in range(Q):
    reqsize, idx = input().split()
    idx = int(idx)-1
    req[idx] = min(req[idx], sizedict[reqsize])

print(sum(size[i] >= req[i] for i in range(n)))