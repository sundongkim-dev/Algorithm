'''
풀이 시작 시간: 2022-10-19 16:31
풀이 종료 시간: 2022-10-19 16:45

시간 제한 1초
메모리 제한 128MB

입력
첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어집니다. (1≤N≤1,000)
둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다. 
이때, 각 화폐 단위는 1,000,000 이하의 자연수입니다.
5
3 2 1 1 9

출력
첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.
8
'''

'''
풀이: 오름 차순 정렬한 뒤에 최적의 해 구하기
'''

N = int(input())
money = list(map(int, input().split()))

money.sort()

answer = 1
for item in money:
    if answer < item:
        break
    answer += item

print(answer)