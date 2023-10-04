# 1차 제출: (65분 소요) 물고기 방향 꺾는거 계산이 안 되서 오래 걸림 & 물고기 잡아먹을 때 부등호 실수 (135148kb, 320ms)
# 2차 제출: from collections import deque 안 지워서 다시 제출 (133556kb, 288ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

R, C, M = map(int, input().split())
matrix = [[None]*C for _ in range(R)]
dt = ((-1,0),(1,0),(0,1),(0,-1))
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[r-1][c-1] = (s,d-1,z)    # 속력, 이동방향, 크기

answer = 0
for fisher in range(C):
    # 고기 잡기
    for r in range(R):
        if matrix[r][fisher]:
            answer += matrix[r][fisher][2]
            matrix[r][fisher] = []
            break
    # 이동
    new_matrix = [[None]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c]:
                s,d,z = matrix[r][c]
                dx, dy = dt[d]
                nx, ny = r+s*dx, c+s*dy

                # 범위 벗어나면 방향 틀어서 이동하는거 처리 (이거 계산하느라 30분 잡은듯)
                while not (0 <= nx < R-1):
                    if nx < 0:
                        nx = -nx
                        if d == 0: d = 1
                    elif nx > R-1:
                        nx = 2*(R-1)-nx
                        if d == 1: d = 0
                    else: break

                while not (0 <= ny < C-1):
                    if ny < 0:
                        ny = -ny
                        if d == 3: d = 2
                    elif ny > C-1:
                        ny = 2*(C-1)-ny
                        if d == 2: d = 3
                    else: break

                # 잡아먹기
                if new_matrix[nx][ny]:
                    if new_matrix[nx][ny][2] < z:
                        new_matrix[nx][ny] = (s,d,z)
                else:
                    new_matrix[nx][ny] = (s,d,z)

    matrix = new_matrix

print(answer)

# 2차 풀이
R, C, M = map(int, input().split())
matrix = [[None for _ in range(C)] for _ in range(R)]
dt = ((-1,0),(1,0),(0,1),(0,-1))
for _ in range(M):
    r, c, s, d, z = map(int, input().split())   # (r,c): 위치, s: 속력, d: 이동방향, z: 크기
    matrix[r-1][c-1] = (s,d-1,z)

answer = 0
for c in range(C):
    # 상어 잡기
    for r in range(R):
        if matrix[r][c] is not None:
            answer += matrix[r][c][-1]
            matrix[r][c] = None
            break

    # 상어 이동
    narr = [[None for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c] is not None:
                s, d, z = matrix[r][c]
                dx, dy = dt[d]

                nx, ny = (r+s*dx)%(2*(R-1)), (c+s*dy)%(2*(C-1))
                if nx > R-1:
                    nx = 2*(R-1)-nx
                    if d == 0: d = 1
                    elif d == 1: d = 0
                if ny > C-1:
                    ny = 2*(C-1)-ny
                    if d == 2: d = 3
                    elif d == 3: d = 2

                if narr[nx][ny] is not None and narr[nx][ny][-1] > z: continue
                narr[nx][ny] = [s,d,z]

    matrix = narr

print(answer)