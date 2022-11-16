'''
출처: Amazon 인터뷰

풀이 시작 시간: 2022-11-16 9:49
풀이 종료 시간: 2022-11-16 9:52

시간 제한: 
메모리 제한: 

입력: 

출력: 

제한사항: O(logN)으로 풀어야 한다.

풀이: 이분탐색으로 푼다.

제출 이력:

'''
def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)

N = int(input())
num = list(map(int, input().split()))

idx = binary_search(arr, 0, N-1)

if idx == 0:
    print(-1)
else:
    print(idx)
