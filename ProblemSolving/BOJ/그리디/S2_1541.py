'''
출처: https://www.acmicpc.net/problem/1541

풀이 시작 시간: 2022-12-08 23:52
풀이 종료 시간: 2022-12-09 00:07

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력: 
첫째 줄에 정답을 출력한다.

제한사항: 

풀이: 
1st / 그리디 알고리즘, -붙은 부분을 괄호 열어서 최대로 만들어주면 됨

제출 이력:
1st / Pass
'''

import sys
input = sys.stdin.readline

f = input().split("-")
answer = 0
for i in f[0].split("+"):
    answer += int(i)

for i in f[1:]:
    print(i)
    for j in i.split("+"):
        answer -= int(j)

print(answer)