'''
풀이 시작 시간: 2022-10-13 22:03
풀이 종료 시간: 2022-10-13 22:11

시간 제한 2초
메모리 제한 128MB

입력
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
4 6
19 15 10 17

출력
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
15
'''

'''
- 파라메트릭 서치, 이진탐색으로 구하기
'''

N, M = map(int, input().split())
li = list(map(int, input().split()))

start=0; end=max(li)
answer = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for item in li:
        if item > mid:
            total += item - mid
    if total < M:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)