import sys

input = sys.stdin.readline

x, y = map(int, input().split())

answer = 0
if x >= y:
    answer += x
    answer += (y // 10)
    answer += y
else:
    answer += y
    answer += (x//10)
    answer += x

print(answer)