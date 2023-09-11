# 1차 제출: 149460kb, 432ms
# 2차 제출: 최종 질량 for문 순회하지 않고 list comprehension으로 sum 구하기 (432ms -> 432ms)
# 3차 제출: dict로 자료 구조 수정 (list보다 구현이 더 어려운 것 같음, 432ms -> 392ms)
# 4차 제출: 파이어볼이 존재하지 않는 경우 조기 종료 조건 추가 (392ms -> 380ms)
# https://www.acmicpc.net/problem/20056
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]
direction = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
for _ in range(M):
    R, C, M, S, D = map(int, input().split())
    matrix[R-1][C-1].append((M,S,D))

for _ in range(K):
    new_matrix = [[[] for _ in range(N)] for _ in range(N)]
    # 이동하기
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                for fire in matrix[r][c]:
                    m, i, dt = fire
                    dx, dy = direction[dt]
                    new_matrix[(r+i*dx)%N][(c+i*dy)%N].append((m,i,dt))
    # 합쳐지기
    for r in range(N):
        for c in range(N):
            if len(new_matrix[r][c]) >= 2:
                m = sum(fire[0] for fire in new_matrix[r][c])//5
                s = sum(fire[1] for fire in new_matrix[r][c])//len(new_matrix[r][c])
                if m:
                    new_d = [fire[2]%2 == 1 for fire in new_matrix[r][c]]
                    if not any(new_d) or all(new_d):
                        new_matrix[r][c] = [(m,s,0),(m,s,2),(m,s,4),(m,s,6)]
                    else:
                        new_matrix[r][c] = [(m,s,1),(m,s,3),(m,s,5),(m,s,7)]
                else: new_matrix[r][c] = []
    matrix = new_matrix

print(sum([f[0] for row in matrix for fire in row for f in fire]))


# 딕셔너리 버전
N, M, K = map(int, input().split())
direction = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
fireballs = {}
for _ in range(M):
    R, C, M, S, D = map(int, input().split())
    fireballs[(R-1,C-1)] = [*fireballs[(R-1,C-1)], (M,S,D)] if (R-1,C-1) in fireballs else [(M,S,D)]

for _ in range(K):
    new_fireballs = {}
    crush = set()
    # 이동하기
    for fireball in fireballs:
        for fire in fireballs[fireball]:
            r, c = fireball
            m, s, d = fire
            dx, dy = direction[d]
            nx, ny = (r+s*dx)%N, (c+s*dy)%N
            if (nx,ny) in new_fireballs:
                new_fireballs[(nx,ny)].append((m,s,d))
                crush.add((nx,ny))
            else:
                new_fireballs[(nx,ny)] = [(m,s,d)]

    # 합쳐지기
    for fire in crush:
        if len(new_fireballs[fire]) >= 2:
            m = sum(fire[0] for fire in new_fireballs[fire])//5
            s = sum(fire[1] for fire in new_fireballs[fire])//len(new_fireballs[fire])
            if m:
                new_d = [fire[2]%2 == 1 for fire in new_fireballs[fire]]
                if not any(new_d) or all(new_d):
                    new_fireballs[fire] = [(m,s,0),(m,s,2),(m,s,4),(m,s,6)]
                else:
                    new_fireballs[fire] = [(m,s,1),(m,s,3),(m,s,5),(m,s,7)]
            else: del new_fireballs[fire]
        else: crush[fire] = new_fireballs[fire]

    fireballs = new_fireballs
    if not new_fireballs: break

answer = 0
for fireball in fireballs:
    answer += sum(fire[0] for fire in fireballs[fireball])
print(answer)