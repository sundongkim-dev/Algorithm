'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60058

풀이 시작 시간: 2022-11-08 22:04
풀이 종료 시간: 2022-11-08 23:03

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:

입출력 예시:
p	= "(()())()"
result = "(()())()"

풀이: 
1st / 문제 입력을 따라서 재귀적으로 구현한다.

제출 이력:
1st / Pass
'''

def chkRight(s):
    cnt = 0
    sLength = len(s)
    for idx in range(sLength):
        if s[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def solution(p):
    answer = ''
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0:
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있음 = 균형잡힌 문자열 완성될때까지 찾기
    open, close = 0, 0
    pLength = len(p)
    u = ""
    v = ""
    for idx in range(pLength):
        if p[idx] == '(':
            open += 1
        else:
            close += 1
        
        if open == close:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if chkRight(u):
        answer += u # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        answer += solution(v)
        return answer
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        tmp = "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        tmp += solution(v)
        # 4-3. ')'를 다시 붙입니다. 
        tmp += ")"
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        u = u[1:]
        u = u[:-1]
        uLength = len(u)
        for idx in range(uLength):
            if u[idx] == '(':
                tmp += ')'
            else:
                tmp += '('
        # 4-5. 생성된 문자열을 반환합니다.     
        return tmp

#p = "(()())()"
p = ")("	
#p ="()))((()"
result = solution(p)

print(result)