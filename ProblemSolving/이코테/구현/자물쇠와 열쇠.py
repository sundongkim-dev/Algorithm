'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60059

풀이 시작 시간: 2022-11-03 18:24
풀이 종료 시간: 2022-11-03 19:47

시간 제한:
메모리 제한: 

입력: 

출력: 

제한사항:
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

입출력 예시:
key	= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
result = true

풀이: 
1st / 완전탐색으로 다 대입해본다.

제출 이력:
1st / Pass
'''


def rotate(key):
    n = len(key)
    result = [[0]*n for _ in range(n)]
    # (0,0) -> (0,n-1) -> (n-1, n-1) -> (n-1, 0) -> (0, 0)
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = key[i][j]
    return result


def chk(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for r in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if chk(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
result = solution(key, lock)
print(result)
