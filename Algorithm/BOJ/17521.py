n, W = map(int, input().split())

market = []
for i in range(n):
    s = int(input())
    market.append(s)

coin = 0
for i in range(n-1):
    if market[i] < market[i+1]:
        if W // market[i] > 0:
            coin = W//market[i]
            W -= market[i] * coin
    elif market[i] > market[i-1]:
        W += coin*market[i]
        coin = 0

W += coin * market[n-1]

print(W)
