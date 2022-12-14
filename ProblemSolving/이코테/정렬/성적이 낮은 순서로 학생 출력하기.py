'''
풀이 시작 시간: 2022-10-13 21:32
풀이 종료 시간: 2022-10-13 21:35

시간 제한 1초
메모리 제한 128MB

입력
첫 번째 줄에 학생의 수 N이 입력된다. (1<=N<=100,000)
두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.
2
홍길동 95
이순신 77

출력
모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
'''

'''
- sort에 key값을 주어서 풀이
'''

N = int(input())
li = []
for _ in range(N):
    name, score = input().split()
    li.append([name, int(score)])

li.sort(key=lambda x : x[1])

for student in li:
    print(student[0], end=' ')