import sys

n , k = map( int , input().split())
p = list(map(int, sys.stdin.readline().rstrip().split()))
max_sum = 0

p.sort(reverse=True)

for i in range(k) :
    max_sum += p[i] - i

print(max_sum)