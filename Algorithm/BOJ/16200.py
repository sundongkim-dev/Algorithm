n = int(input())
x = sorted(map(int,input().split()))

team = 0
i = 0

while i < n:
    team += 1
    i += x[i]

print(team)