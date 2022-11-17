'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

풀이 시작 시간: 2022-11-17 11:08
풀이 종료 시간: 2022-11-17 11:42

시간 제한: 3초
메모리 제한: 256MB

입력: 
가장 첫줄은 전체 테스트 케이스의 수이다.
각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).
그 다음 N개의 줄에 걸쳐 N x M 크기의 직사각형 배열이 주어진다.

출력: 
각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.
주어진 암호코드가 올바른 암호코드일 경우, 암호코드에 포함된 숫자의 합을 출력하라. 만약 잘못된 암호코드일 경우 대신 0을 출력하라.

제한사항: 

풀이: 
1st / 지문대로 구현

제출 이력:
1st / Pass
'''

password = {"0001101": 0, "0011001":1, "0010011":2, "0111101":3,"0100011":4, 
            "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}
zero = "0"
for tc in range(1,int(input())+1):
    answer, odd, even = -1, 0, 0
    n, m = map(int, input().split())

    for i in range(n):
        s = input()
        if int(s) != 0 and answer == -1:
            s = str(int(s[::-1]))
            
            tmp = []
            for j in range(8):
                tmp.insert(0, password[(s[7*j :7*j+7])[::-1]])
            
            SUM = (tmp[0]+tmp[2]+tmp[4]+tmp[6])*3 + tmp[1] + tmp[3] + tmp[5] + tmp[7]
            if SUM%10 == 0:
                answer = sum(tmp)
            else:
                answer = 0
                
    print('#{} {}'.format(tc, answer))