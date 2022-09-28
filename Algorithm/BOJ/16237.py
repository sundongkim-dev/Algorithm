a,b,c,d,e = map(int, input().split())

answer = d+e

# d 담기, a 있다면 한개씩 같이 넣기
if a <= d:
    a = 0
else:
    a -= d

# c 담기, b 있다면 한개씩 같이 넣기, 없다면 A 2개씩 넣기
answer += c
if b >= c:
    b -= c
    answer += b//2 + b%2
    a -= (b//2)
    if b%2:
        a -= 3
# b 담기, c 있다면 한개씩 넣기, 없다면 A 3개씩 넣기
else:
    c -= b
    a -= (c*2)
# a 남아있으면 다 담기
if a > 0:
    answer += (a//5)
    if a%5 > 0:
        answer += 1

print(answer)