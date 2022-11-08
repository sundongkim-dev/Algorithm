while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break

    li = sorted(li[1:])
    zeros = li.count(0)
    a = ''; b = ''
    for i in range(zeros, len(li)):
        if (zeros - i) % 2 == 0:
            a += str(li[i])
        else:
            b += str(li[i])
    da = a; db = b
    for i in range(zeros):
        if len(a) == len(b):
            if i % 2 == 0:
                da = da[0] + '0' + da[1:]
            else:
                db = db[0] + '0' + db[1:]
        else:   
            if i % 2 == 0:
                db = db[0] + '0' + db[1:]       
            else:
                da = da[0] + '0' + da[1:]           
    print(int(da)+int(db))
            