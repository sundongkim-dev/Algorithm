N = int(input())

answer = (N-1) // 9 + 1
if answer%2 == 0 and N%2 == 1:
    answer += 1

print(answer)