'''
출처: https://www.acmicpc.net/problem/2493

풀이 시작 시간: 2022-12-01 12:43
풀이 종료 시간: 2022-12-01 12:52

시간 제한: 5초
메모리 제한: 128MB

입력: 
첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. N은 1 이상 500,000 이하이다. 
둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.

출력: 
첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.

제한사항: 

풀이: 
1st / stack 활용하여 풀이

제출 이력:
1st / Pass
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
s = []
answer = []
for i in range(n):
    while s:
        if s[-1][1] > graph[i]:
            answer.append(s[-1][0] + 1)
            break
        else:
            s.pop()
    if not s:
        answer.append(0)
    s.append([i, graph[i]])
print(" ".join(map(str, answer)))