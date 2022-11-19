'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14w-rKAHACFAYD&categoryId=AV14w-rKAHACFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 16:21
풀이 종료 시간: 2022-11-19 16:43

시간 제한: 10개/30초
메모리 제한: 256MB

입력: 
첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
두 번째 줄 : 원본 암호문
세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
네 번째 줄 : 명령어
위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.

출력: 
#기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.

제한사항:

풀이: 
1st / 문제대로 구현

제출 이력:
1st / Pass
'''

for tc in range(1, 11):
    n = int(input())
    originalCMD = input().split()
    
    c = int(input())
    cmd = input().split()
    
    for idx, item in enumerate(cmd):
        if item == "I":
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            s = cmd[idx+3:idx+3+y]
            for index, j in enumerate(s):
                originalCMD.insert(x+index,j)
    
    print("#{} ".format(tc),end='')
    print(*originalCMD[:10])
    