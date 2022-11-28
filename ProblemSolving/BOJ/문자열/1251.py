'''
출처: https://www.acmicpc.net/problem/1251

풀이 시작 시간: 2022-11-28 21:45
풀이 종료 시간: 2022-11-28 21:53

시간 제한: 2초
메모리 제한: 128MB

입력: 
첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다.

출력: 
첫째 줄에 구하고자 하는 단어를 출력하면 된다.

제한사항: 

풀이: 
1st / 문자열 브루트포스

제출 이력:
1st / Pass
'''

s = input()
length = len(s)
answer = []
for i in range(1, length-1):
    for j in range(i+1, length):
        a = s[:i][::-1]
        b = s[i:j][::-1]
        c = s[j:][::-1]
        answer.append(a+b+c)
answer.sort()
print(answer[0])
        #print(s[:i], s[i:j], s[j:])