from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

Ali = list(map(int, input().split()))
Bli = list(map(int, input().split()))

Acounter = Counter(Ali)
Bcounter = Counter(Bli)
ABcounter = Acounter - Bcounter
print(sum(ABcounter.values()))