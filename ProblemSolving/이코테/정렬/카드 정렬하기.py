'''
출처: https://www.acmicpc.net/problem/1715

풀이 시작 시간: 2022-11-15 22:30
풀이 종료 시간: 2022-11-15 22:

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 
숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

출력: 
첫째 줄에 최소 비교 횟수를 출력한다.

제한사항:

풀이: 
1st / 우선순위 큐를 이용해서 제일 작은 것끼리 계속 더해준다.

제출 이력:
1st / Pass
'''
import heapq

N = int(input())
answer = 0
deck = []
for _ in range(N):
    heapq.heappush(deck, int(input()))

while len(deck) != 1:
    num1 = heapq.heappop(deck)
    num2 = heapq.heappop(deck)
    answer += (num1+num2)
    heapq.heappush(deck, num1+num2)

print(answer)