N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)] # r c m s d
graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 이동을 k번 명령한 후, 남아있는 파이어볼의 질량의 합
for _ in range(K):

    # 이동 명령
    while fireball:
        # step1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다
        # 이동하는 중에 같은 칸에 여러 개의 파이어볼이 있을 수 있다
        cr, cc, cm, cs, cd = fireball.pop(0)
        nr = (cr + cs * dx[cd]) % N  
        nc = (cc + cs * dy[cd]) % N
        graph[nr][nc].append([cm, cs, cd]) # 해당 위치에 파이어볼 질량, 속도, 방향 기록
    
    # step2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서 다음과 같은 일이 일어난다
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2: # 2개 이상의 파이어볼
                # step2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다            
                # step2-2. 파이어볼은 4개의 파이어볼로 나누어진다
                # step2-3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
                m_sum, s_sum, dir_odd, dir_even, dir_cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    m, s, d = graph[i][j].pop(0)
                    m_sum += m
                    s_sum += s
                    if d%2 == 0: # 방향 인덱스 0부터 시작하므로
                        dir_odd += 1
                    else:
                        dir_even += 1
                    if dir_odd == dir_cnt or dir_even == dir_cnt: # 방향 모두 짝수이거나 모두 홀수인 경우
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5 ,7]
                m_division = m_sum // 5         # 질량은 floor((파이어볼 질량의 합)/5)
                s_division = s_sum // dir_cnt   # 속력은 floor((합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수))
                # setp2-4. 질량이 0인 파이어볼은 소멸되어 없어진다
                if m_division == 0:
                    continue
                else:
                    for direction in nd:
                        fireball.append([i, j, m_division, s_division, direction])
            # 파이어볼 1개인 경우는 그냥 이동
            elif len(graph[i][j]) == 1:
                fireball.append([i,j] + graph[i][j].pop())
    
answer = 0
for fb in fireball:
    answer += fb[2]
print(answer)
            