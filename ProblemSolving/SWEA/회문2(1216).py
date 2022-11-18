'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-18 20:31
풀이 종료 시간: 2022-11-18 21:00

시간 제한: 10개/30초
메모리 제한: 256MB

입력: 
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

출력: 
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.

제한사항:
각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다. 

풀이: 
1st / 

제출 이력:
1st / Pass
'''

def find_palindrome(sentences):
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(100-k+1):
                if sentences[i][j] == sentences[i][j+k-1]:
                    left = j
                    right = j+k-1
                    while sentences[i][left] == sentences[i][right] and left <= right:
                        left += 1
                        right -= 1
                    if left < right:
                        continue
                    else:
                        max_length = k
                        return max_length


for _ in range(10):
    tc = int(input())
    graph = [list(input().rstrip()) for _ in range(100)]
    result1 = find_palindrome(graph)
    reverse_graph = list(zip(*graph))
    result2 = find_palindrome(reverse_graph)
    answer = max(result1, result2)
    print("#{} {}".format(tc, answer))