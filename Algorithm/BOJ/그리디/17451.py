n = int(input())
li = list(map(int,input().split()))
speed = li[-1]

for i in range(n-2, -1, -1): 
    if li[i] > speed: 
        speed = li[i] 
    else: 
        if speed%li[i]:
            speed = (speed//li[i]+1) *li[i]
            
print(speed)