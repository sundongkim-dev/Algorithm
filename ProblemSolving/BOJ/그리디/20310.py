s = input()

ones_erase = s.count("1")//2
zeros_erase = s.count("0")//2

li = list(s)

for i in range(ones_erase):
    for idx in range(len(li)):
        if li[idx] == "1":
            li.pop(idx)
            break

for i in range(zeros_erase):
    for idx in range(len(li)-1, -1, -1):
        if li[idx] == "0":
            li.pop(idx)
            break

print(''.join(li))