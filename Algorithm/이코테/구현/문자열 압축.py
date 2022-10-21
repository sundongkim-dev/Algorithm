'''
풀이 시작 시간: 2022-10-21 17:51
풀이 종료 시간: 2022-10-21 18:23

https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

풀이: 패턴만큼 끊어서 반복하여 모든 경우의 수의 길이를 다 구한다

Fail/1st: 런타임 에러 -> 길이가 1인 경우 li가 비어있게 되는데 이때는 1을 return 해주어야 한다.
Pass/2nd
'''

def solution(s):
    answer = 0
    li = []
    for i in range(1, len(s)//2+1):
        
        pattern = s[:i]
        patternLength = len(pattern)
        cnt = 1
        tmp = ""
        for j in range(i, len(s), patternLength):
            if pattern == s[j:j+patternLength]:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += (str(cnt) + pattern)
                else:
                    tmp += pattern    
                cnt = 1
                pattern = s[j:j+patternLength]

        if cnt > 1:
            tmp += (str(cnt) + pattern)
        else:
            tmp += pattern
        li.append(len(tmp))
    
    if len(li) == 0:
        return 1
    else:
        return min(li)

s = "a"	
print(solution(s))