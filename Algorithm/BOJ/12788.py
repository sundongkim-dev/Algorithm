N = int(input())
M, K = map(int, input().split())
li = list(map(int, input().split()))

li.sort(reverse=True)

answer = cur = 0
need = M*K

for item in li:
    cur += item
    answer += 1
    if cur >= need:
        print(answer)
        break
else:
    print("STRESS")