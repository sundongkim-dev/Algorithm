N = int(input())

li = [input() for _ in range(N)]

sizeDict = {'1/4':0, '1/2':0, '3/4': 0}

for item in li:
    sizeDict[item] += 1

a = sizeDict['1/4']
b = sizeDict['1/2']
c = sizeDict['3/4']

answer = c

# 3/4 담기, 1/4 있다면 한 개씩 같이 넣기
if a <= c:
    a = 0
else:
    a -= c

# 1/2 담기, 1/2 있다면 한 개씩 같이 넣기, 없다면 1/4 두 개씩 넣기
if b % 2 == 0:              # 1/2 2의 배수로 존재하면 싹 다 넣기, 1/4 고려할 필요 없음
    answer += b//2
else:                       # 1/2 2의 배수가 아니라면 2로 나눈 몫만큼 더해주고 1/4 2개 있다면 같이 넣어주기
    answer += b//2 + b%2    
    # 1/4 두 개 있는 경우
    if a >= 2:
        a -= 2
    elif a == 1:
        a -= 1
# 남은 a 있다면 다 넣어주기    
if a > 0:
    answer += a//4
    if a%4 > 0:
        answer += 1

print(answer)