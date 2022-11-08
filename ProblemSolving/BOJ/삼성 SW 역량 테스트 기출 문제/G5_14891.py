'''
풀이 시작 시간: 2022-10-14 19:07
풀이 종료 시간: 2022-10-14 20:10

시간 제한 2초
메모리 제한 512MB

입력
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

출력
총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''

'''
- deque와 재귀를 사용해서 회전 후 판단하는 것으로 구현
Pass/1st
'''

# N극은 0, S극은 1
from collections import deque

def rotate_right(x, d):
    # 같으면 멈춤
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        rotate_right(x + 1, -d)
        gears[x].rotate(d)

def rotate_left(x, d):
    # 같으면 멈춤
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return

    if gears[x][2] != gears[x + 1][6]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))

for _ in range(int(input())):
    gearNum, d = map(int, input().split())

    rotate_right(gearNum + 1, -d)
    rotate_left(gearNum - 1, -d)
    gears[gearNum].rotate(d)

ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)

print(ans)