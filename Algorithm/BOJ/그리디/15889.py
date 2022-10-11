N = int(input())
li = list(map(int, input().split()))
if N!=1:
    tmp = list(map(int, input().split()))

    maxLength = 0

    for i in range(1, N):
        if maxLength < li[i-1]+tmp[i-1]:
            maxLength = li[i-1]+tmp[i-1]
        if maxLength < li[i]:
            print("엄마 나 전역 늦어질 것 같아")
            break
    else:
        print("권병장님, 중대장님이 찾으십니다")
else:
    print("권병장님, 중대장님이 찾으십니다")
