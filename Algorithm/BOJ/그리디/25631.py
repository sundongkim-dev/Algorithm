from sys import stdin
from collections import Counter

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

counter = Counter(seq)

print(max(counter.values()))