import sys

input=sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

"""
B배열 재배열 금지
"""
a.sort()
# b.sort(reverse=True)

# answer = 0
# for x, y in zip(a,b):
#     answer += (x*y)

# print(answer)

answer = 0
for i in range(N):
    answer += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(answer)