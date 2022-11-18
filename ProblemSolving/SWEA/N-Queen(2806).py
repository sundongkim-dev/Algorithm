'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-17 12:06
풀이 종료 시간: 2022-11-17 13:11

시간 제한: 10/8초
메모리 제한: 256MB

입력: 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.

출력: 
각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

제한사항:

풀이: 
1st / 백트래킹

제출 이력:
1st / Pass
'''

def func(cur):
    global answer, n
    if cur == n:
        answer += 1
        return;
    for i in range(n):
        if isused1[i] or isused2[i+cur] or isused3[cur-i+n-1]:
            continue
        isused1[i] = True
        isused2[i+cur] = True
        isused3[cur-i+n-1] = True
        func(cur+1)
        isused1[i] = False
        isused2[i+cur] = False
        isused3[cur-i+n-1] = False

for tc in range(1, int(input())+1):
    answer = 0
    n = int(input())
    
    isused1 = [False]*20
    isused2 = [False]*20
    isused3 = [False]*20
    
    func(0)

    print("#{} {}".format(tc, answer))