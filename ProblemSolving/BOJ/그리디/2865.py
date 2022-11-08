import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

candidate_score = {}
for i in range(N):
    candidate_score[i+1] = 0

for i in range(M):
    genre = list(map(float, input().split()))
    
    for j in range(0, 2*N, 2):
        if genre[j+1] > candidate_score[genre[j]]:
            candidate_score[genre[j]] = genre[j+1]

score = sorted(list(candidate_score.values()), reverse=True)
sum = sum(score[:K])
print('%.1f' % sum)