from collections import Counter

s = input()

li = sorted(Counter(s).items())

flag = False
for i in li:
    if i[1]%2 == 1:
        if flag == True:
            print("I'm Sorry Hansoo")
            break
        else:
            flag = True
else:
    # 팰린드롬 만들어서 출력
    answer = ""
    tmp1 = ""
    tmp2 = ""
    ch = ""
    for i in li:
        num = i[1]
        # num이 짝수면 좌우 분배
        if num%2 == 0:
            tmp1 += i[0]*(num//2)
            tmp2 = i[0]*(num//2) + tmp2
        # num이 홀수면 가운데에 배치해야하므로 기억하기
        else:
            ch = i[0]
            tmp1 += i[0]*(num//2)
            tmp2 = i[0]*(num//2) + tmp2
    answer = tmp1 + ch + tmp2
    print(answer)
