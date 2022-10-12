import sys

input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]

li.sort()

rank = 1; answer = 0
for item in li:
    answer += abs(item - rank)
    rank += 1

print(answer)