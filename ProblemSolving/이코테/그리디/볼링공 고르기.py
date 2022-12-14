'''
풀이 시작 시간: 2022-10-19 16:46
풀이 종료 시간: 2022-10-19 16:53

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다. (1 ≤ N ≤ 1,000, 1 ≤ M ≤ 10)
둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다. (1 ≤ K ≤ M)
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

출력
첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.
8

25
'''

'''
풀이: 경우의 수를 줄여주면서 곱해주면 된다.
'''

N, M = map(int, input().split())
K = list(map(int, input().split()))

arr = [0]*11
for i in K:
    arr[i] += 1

answer = 0
for i in range(1, M+1):
    N -= arr[i]
    answer += arr[i]*N

print(answer) 