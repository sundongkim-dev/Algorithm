'''
출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

풀이 시작 시간: 2022-11-19 17:13
풀이 종료 시간: 2022-11-19 18:43

시간 제한: 20개/16초
메모리 제한: 256MB

입력: 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 정수 H, W (2 ≤ H, W ≤ 20) 이 공백으로 구분되어 주어진다.
이는 게임 맵의 높이가 H, 너비가 W임을 나타낸다.
즉, 게임 맵은 H x W크기의 격자판이다.
다음 H개의 각각의 줄에는 길이가 W인 문자열이 주어진다.
각각의 문자는 위의 게임 맵 구성 요소 표에 있는 문자들만 포함하며, 전차는 단 하나만 있다.
다음 줄에는 사용자가 넣을 입력의 개수를 나타내는 정수 N(0 < N ≤ 100) 이 주어진다.
다음 줄에는 길이가 N인 문자열이 주어진다.
각각의 문자는 위의 사용자가 넣을 수 있는 입력의 종류를 나타내는 표에 있는 문자들만 포함된다.

출력: 
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후, 모든 입력을 처리하고 난 후의 게임 맵을 H개의 줄에 걸쳐 출력한다.

제한사항:

풀이: 
1st / 풀이대로 구현

제출 이력:
1st / Pass
'''

dirInfo = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dic = {"^": 0, ">": 1, "v": 2, "<": 3}  # 위 오 아 왼
dicRev = {0: "^", 1: ">", 2: "v", 3: "<"}  # 위 오 아 왼

def move(direction):
    global tank, graph, H, W, tankdir
    tankdir = direction
    x, y = tank
    nx, ny = x+dirInfo[tankdir][0], y+dirInfo[tankdir][1]
    graph[x][y] = dicRev[tankdir]
    if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == ".":
        tank = [nx, ny]
        graph[x][y] = "."
        graph[nx][ny] = dicRev[tankdir]


for tc in range(1, int(input())+1):
    answer = 0
    H, W = map(int, input().split())
    graph, tank = [], []
    tankdir = -1
    flag = False
    for idx in range(H):
        info = list(input())
        for j, item in enumerate(info):
            if flag:
                break
            if item == "^" or item == "v" or item == "<" or item == ">":
                tank = [idx, j]
                tankdir = dic[item]
                flag = True
        graph.append(info)

    N = int(input())
    cmd = input()

    for c in cmd:
        if c == "S":
            x, y = tank[0], tank[1]
            while True:
                x, y = x+dirInfo[tankdir][0], y+dirInfo[tankdir][1]
                if 0>x or x>=H or 0>y or y>=W or graph[x][y] == "#":
                    break
                if graph[x][y] == "*":
                    graph[x][y] = "."
                    break        
        elif c == "U":
            move(0)
        elif c == "R":
            move(1)
        elif c == "D":
            move(2)
        elif c == "L":
            move(3)

    print("#{}".format(tc), end=' ')
    for item in graph:
        print("".join(item))
