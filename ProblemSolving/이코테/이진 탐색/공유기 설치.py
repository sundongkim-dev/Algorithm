'''
출처: https://www.acmicpc.net/problem/2110

풀이 시작 시간: 2022-11-16 9:58
풀이 종료 시간: 2022-11-16 10:19

시간 제한: 2초
메모리 제한: 128MB

입력: 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력: 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

제한사항: 

풀이: 
1st / 이분탐색으로 푼다.
2nd / sys readline 쓰기

제출 이력:
1st / 시간 초과
2nd / Pass

'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

graph = sorted([int(input()) for _ in range(N)])

start = 1
end = graph[-1] - graph[0]
answer = 0

while start <= end:
    mid = (start+end)//2
    val = graph[0]
    cnt = 1
    for i in range(1, N):
        if graph[i] >= val + mid:
            val = graph[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
 
print(answer)