N, K = map(int, input().split())
li = list(input())
visited = [False]*N

answer = 0
for i in range(N):
    # 사람인 경우만 확인
    if li[i] == 'P':
        # 왼쪽 먼저 확인, K거리만큼부터 확인
        for j in range(i-K, i+K+1):
            if j < 0 or j > N-1 or j==i:
                continue
            # 유효한 인덱스면 검토
            else:
                # 햄버거이면서 누가 먹지 않았어야 한다
                if li[j] == 'H' and visited[j] == False:
                    answer += 1
                    visited[j] = True
                    break
print(answer)

