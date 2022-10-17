'''
풀이 시작 시간: 2022-10-17 13:23
풀이 종료 시간: 2022-10-17 13:46

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 N(2<=N<1,000), M(1<=M<=10,000), K(1<=K<=10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.
단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.
5 8 3
2 4 5 4 6

출력
첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다. 
46
'''
'''
풀이: 제일 큰 수를 K번 더하고 두 번째로 큰 수를 더한다. 더해지는 횟수가 총 M이 되도록 반복한다
'''

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
answer = 0

# answer = data[0]
# for idx in range(1, M):
#     if idx%K == 0:
#         answer += data[1]
#     else:
#         answer += data[0]

first = data[0]
second = data[1]

cnt = int(M/(K+1)) * K + M%(K+1)
answer += cnt*first + (M-cnt)*second
print(answer)