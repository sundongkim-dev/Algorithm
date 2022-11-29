'''
출처: https://www.acmicpc.net/problem/2263

풀이 시작 시간: 2022-11-29 13:15
풀이 종료 시간: 2022-11-22 13:38

시간 제한: 5초
메모리 제한: 128MB

입력: 
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

출력: 
첫째 줄에 프리오더를 출력한다.

제한사항: 

풀이: 
1st / 분할 정복으로 프리 오더 찾기

제출 이력:
1st / Pass
'''

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def preorder(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end):
        return

    parent = postorder[post_end]
    print(parent, end=" ")

    left = position[parent] - in_start
    right = in_end - position[parent]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i
preorder(0, n-1, 0, n-1)