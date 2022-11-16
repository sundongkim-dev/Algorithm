'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&

풀이 시작 시간: 2022-11-16 23:44
풀이 종료 시간: 2022-11-16 00:11

시간 제한: 2초
메모리 제한: 256MB

입력: 
가장 첫 줄은 전체 테스트 케이스의 수이다.
최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.
각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

출력: 
각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.
같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.


제한사항: 

풀이: 
1st / 완전탐색

제출 이력:
1st / Pass
'''

for tc in range(1,int(input())+1):
    data, K = input().split()
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc, max(map(int,now))))