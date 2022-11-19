'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 21:06
풀이 종료 시간: 2022-11-19 21:22

시간 제한: 10개/30초
메모리 제한: 256MB

입력: 
10개의 테스트 케이스가 10줄에 걸쳐, 한 줄에 테스트 케이스 하나씩 제공된다.
각 테스트 케이스는 우선 문자열이 포함하는 문자의 총 수가 주어지고, 공백을 둔 다음 번호 문자열이 공백 없이 제공된다.
문자열은 0~9로 구성되며 문자열의 길이 N은 10≤N≤100이다. 비밀번호의 길이는 문자열의 길이보다 작다.

출력:
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(비밀번호)을 출력한다.

제한사항:

풀이: 
1st / 구현

제출 이력:
1st / Pass
'''

for tc in range(1, 11):
    answer = 0
    n, s = input().split()
    n = int(n)
    s = list(s)
    num = len(s)
    while True:
        length = len(s) - 1
        for i in range(length):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                break
        if num == len(s):
            break
        num = len(s)
    print("#{} {}".format(tc, "".join(s)))