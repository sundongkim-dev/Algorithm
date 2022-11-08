import sys

input=sys.stdin.readline

"""
시간초과
"""

# from itertools import permutations

# N = list(input())

# answer = -1
# for i in permutations(N, len(N)):
#     s = int(''.join(i))
#     if s % 30 == 0:
#         answer = max(answer, s)

# print(answer)

N = list(input().rstrip())

N.sort(reverse=True)

if N[-1]!='0' or sum(map(int,N))%3!=0:
    print(-1)
else:
    print(''.join(N))

