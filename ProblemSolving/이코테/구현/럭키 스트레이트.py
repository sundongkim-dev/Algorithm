'''
풀이 시작 시간: 2022-10-21 17:29
풀이 종료 시간: 2022-10-21 17:37

시간 제한 1초
메모리 제한 256MB

입력
첫째 줄에 점수 N이 정수로 주어진다. (10 ≤ N ≤ 99,999,999) 
단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

출력
첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다.

풀이: 반을 나눠서 더한 값을 비교해준다.
'''

N = input()
sum1 = sum2 = 0
for i in range(len(N)//2):
    sum1 += int(N[i])

for i in range(len(N)//2, len(N), 1):
    sum2 += int(N[i])

answer = "LUCKY" if sum1 == sum2 else "READY"
print(answer)