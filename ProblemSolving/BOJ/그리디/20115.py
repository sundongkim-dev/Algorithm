N = int(input())
li = list(map(int, input().split()))

max_num = max(li)
del li[li.index(max_num)]

for item in li:
    max_num += item/2

print(max_num)
