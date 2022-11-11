'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/42889

풀이 시작 시간: 2022-11-11 10:20
풀이 종료 시간: 2022-11-11 10:55

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

입출력 예시:
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = [3,4,2,1,5]

풀이: 
1st / count를 사용하여 실패율을 계산하고 정렬하여 반환한다.

제출 이력:
1st / Pass
'''

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = solution(N, stages)
print(result)