'''
출처: https://www.acmicpc.net/problem/9012

풀이 시작 시간: 2022-11-22 01:50
풀이 종료 시간: 2022-11-22 02:02

시간 제한: 1초
메모리 제한: 128MB

입력: 
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력: 
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

제한사항: 

풀이: 
1st / 스택사용하여 구현

제출 이력:
1st / Pass
'''

t = int(input())
for i in range(t):
    s = list(input())
    top = 0
    for i in s:
        if i == '(':
            top += 1
        else:
            top -= 1
            if top < 0:
                break
    if top == 0:
        print("YES")
    else:
        print("NO")