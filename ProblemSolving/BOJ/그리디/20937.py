import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

li.sort()

licounter = Counter(li)

print(licounter.most_common(1)[0][1])