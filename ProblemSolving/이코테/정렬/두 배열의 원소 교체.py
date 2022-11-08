'''
풀이 시작 시간: 2022-10-13 21:37
풀이 종료 시간: 2022-10-13 21:40

시간 제한 1초
메모리 제한 128MB

입력
첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1<=N<=100,000, 0<=K<=N)
두 번째 줄에 배열 A의 원소들이 공백으로 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
세 번째 줄에 배열 B의 원소들이 공백으로 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
5 3
1 2 5 4 3
5 5 6 6 5

출력
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.
26
'''

'''
- 각각 오름차순, 내림차순해서 swap
'''

N, K = map(int, input().split())
ali = list(map(int, input().split()))
bli = list(map(int, input().split()))

ali.sort()
bli.sort(reverse=True)

for idx in range(N):
    if K == 0 or ali[idx] >= bli[idx]:
        break
    ali[idx], bli[idx] = bli[idx], ali[idx]
    K -= 1

print(sum(ali))
