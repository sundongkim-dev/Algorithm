N = int(input())
road = list(map(int, input().split()))
price = list(map(int,input().split()))

min_price = price[0]
sum = price[0]*road[0]

for i in range(1,N-1):
    if min_price > price[i]:
        min_price = price[i]
    sum += min_price*road[i]
    
print(sum)