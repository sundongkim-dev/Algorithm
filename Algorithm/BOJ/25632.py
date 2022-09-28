import math
from collections import Counter

yt = 0
yj = 0

a, b = map(int, input().split())
c, d = map(int, input().split())

n = 1000
li = [True for x in range(n+1)]
li[0] = li[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    j = 2
    while i*j <= n:
        li[i*j] = False
        j += 1

yt_li = []
yj_li = []

for i in range(a, b+1):
    if li[i] == True:
        yt_li.append(i)

for i in range(c, d+1):
    if li[i] == True:
        yj_li.append(i)

yt_counter = Counter(yt_li)
yj_counter = Counter(yj_li)

andcounter = yt_counter & yj_counter
andli = list(andcounter.keys())

yt_counter -= andcounter
yj_counter -= andcounter

if len(andli) % 2 == 0:
    if len(yt_counter.keys()) > len(yj_counter.keys()):
        print("yt")
    else:
        print("yj")
else:
    if len(yt_counter.keys()) >= len(yj_counter.keys()):
        print("yt")
    else:
        print("yj")


