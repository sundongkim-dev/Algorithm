A, K = map(int, input().split())

answer = 0

while A != K:
    # 2로 나누어지면 나누고 나눴는데 A보다 작으면 1 빼준다.
    if K%2==0 and K//2 >= A:
        K = K//2
        answer += 1
    else:
        K -= 1
        answer += 1

print(answer)
