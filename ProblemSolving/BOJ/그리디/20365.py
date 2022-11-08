N = int(input())
s = input()

answer1 = answer2 = 0
length = len(s)
flag = False

answer1 += 1
for idx in range(length):
    if s[idx] == "B":
        if flag == True:
            flag = False
        continue
    else:
        if flag == False:
            flag = True
            answer1 += 1
        else:
            pass
        
flag = False
answer2 += 1
for idx in range(length):
    if s[idx] == "R":
        if flag == True:
            flag = False
        continue
    else:
        if flag == False:
            flag = True
            answer2 += 1
        else:
            pass

print(min(answer1, answer2))
