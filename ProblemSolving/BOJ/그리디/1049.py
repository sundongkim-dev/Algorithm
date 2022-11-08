N, M = map(int, input().split())

# 패키지는 6개, 낱개는 1개
package = ea = 1000

li = []
for _ in range(M):
    a, b = map(int, input().split())
    package = min(package, a)
    ea = min(ea, b)

# 모든 케이스 비교
print(min((N//6)*package + (N%6)*ea, min(N*ea, (N//6+1)*package)))