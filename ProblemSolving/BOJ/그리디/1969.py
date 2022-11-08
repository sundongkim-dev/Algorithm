from collections import Counter

n, m = map(int, input().split())

dnalist = []

for i in range(n):
    dnalist.append(input())

num = n
ans_num = 0
ans_str = ""
for i in range(m):
    ls = []
    for j in range(n):
        ls.append(dnalist[j][i])
    ls.sort()
    counter = Counter(ls)
    counter = counter.most_common(1)
    ans_str += str(counter[0][0])
    ans_num += (num-counter[0][1])

print(ans_str)
print(ans_num)