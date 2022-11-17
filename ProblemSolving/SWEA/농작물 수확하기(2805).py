'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

풀이 시작 시간: 2022-11-17 11:44
풀이 종료 시간: 2022-11-17 12:04

시간 제한: 50/4초
메모리 제한: 256MB

입력: 
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

출력: 
각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

제한사항: 
농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.

풀이: 
1st / 지문대로 구현

제출 이력:
1st / Pass
'''

for tc in range(1, int(input())+1):
    answer = 0
    n = int(input())
    
    farm = []
    for idx in range(n):
        li = list(input())
        for pos in range(n):
            li[pos] = int(li[pos])
        farm.append(li)
        
    if n == 1:
        answer = farm[0][0]
        print("#{} {}".format(tc, answer))
        continue
    
    start = n // 2
    end = start + 1
    for i in range(n//2+1):
        answer += sum(farm[i][start:end])
        start -= 1
        end += 1
    start += 1
    end -= 1
    for i in range(n//2+1, n):
        start += 1
        end -= 1
        answer += sum(farm[i][start:end])
    
    print("#{} {}".format(tc, answer))