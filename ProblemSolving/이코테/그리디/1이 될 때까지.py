'''
풀이 시작 시간: 2022-10-17 13:57
풀이 종료 시간: 2022-10-17 14:00

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 N(2<=N<=100,000)과 K(2<=K<=100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
25 5

출력
첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
2
'''

'''
풀이: K로 나눠지면 나누고 그렇지 않으면 1을 빼는 것을 반복한다.
'''

N, K = list(map(int, input().split()))
answer = 0

# while N != 1:
#     if N%K == 0:
#         N = N // K
#     else:
#         N -= 1
#     answer += 1

while True:
    target = (N//K)*K
    answer += (N-target)
    N = target
    if N<K:
        break
    answer += 1
    N //= K

answer += (N-1)
print(answer)