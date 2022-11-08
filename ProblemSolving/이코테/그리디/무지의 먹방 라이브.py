'''
https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

풀이 시작 시간: 2022-10-17 14:12
풀이 종료 시간: 2022-10-17 14:44

시간 제한 1초
메모리 제한 128MB

'''

'''
풀이: 우선순위 큐를 사용해서 최저 값을 한번에 빼주는 것을 반복하여 구한다.
'''
import heapq

def solution(food_times, k):
    answer = -1
    q = []
    
    foods = len(food_times)
        
    for idx in range(foods):
        heapq.heappush(q, (food_times[idx], idx+1))
    
    length = len(q)
    prev = 0

    while q:
        gap = (q[0][0] - prev) * length
        if gap <= k:
            k -= gap
            length -= 1
            prev, _ = heapq.heappop(q)
        else:
            idx = k % length
            q.sort(key = lambda x : x[1])
            answer = q[idx][1]
            break

    return answer

food_times = [3,1,2]
k = 5
result = solution(food_times, k)
print(result)