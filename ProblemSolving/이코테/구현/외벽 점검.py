'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60062

풀이 시작 시간: 2022-11-04 18:20
풀이 종료 시간: 2022-11-04 19:56

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:
n은 1 이상 200 이하인 자연수입니다.
weak의 길이는 1 이상 15 이하입니다.
서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
weak의 원소는 0 이상 n - 1 이하인 정수입니다.
dist의 길이는 1 이상 8 이하입니다.
dist의 원소는 1 이상 100 이하인 자연수입니다.
친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

입출력 예시:
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
result = 2

풀이: 
1st / 완전탐색으로 다 대입해본다. 다만 원형인 점을 고려해서 weak 배열을 두배로 만들어준다.

제출 이력:
1st / 
'''

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i]+n)
    
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1

    return answer
    
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
result = solution(n, weak, dist)
print(result)