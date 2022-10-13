'''
풀이 시작 시간: 2022-10-13 21:51
풀이 종료 시간: 2022-10-13 21:59

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다. (1<=N<=100,000)
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
5
8 3 7 9 2
3
5 7 9

출력
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
no yes yes
'''

'''
- 부품 배열 정리하고 이진 탐색으로 서치
- set을 활용하여 탐색
'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

N = int(input())
li = list(map(int, input().split()))
li.sort()

M = int(input())
request = list(map(int, input().split()))

for item in request:
    answer = binary_search(li, item, 0, N-1)
    if answer != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')