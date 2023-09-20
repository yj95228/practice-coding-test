# https://www.acmicpc.net/problem/19237
'''
1차 제출: 소요시간 거의 하루 종일..??
- 상어 냄새 경로 기록 등등 자료 구조 관리가 너무 까다로웠음
- 코드 새로 갈아엎고 다시 짰지만 그래도 너무 더럽다
- 마지막에 냄새 배열 부등호 실수함
'''
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]        # 상어 위치
shark = [[] for _ in range(M)]                                      # 상어 냄새 경로
smell = [[[] for _ in range(N)] for _ in range(N)]                  # 상어 냄새 배열

for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            m = matrix[r][c]-1
            shark[m].append((r,c))
            smell[r][c].append(m)

dead = [False]*M                                                    # 상어 격자 내에 있는지
dt = ((-1,0),(1,0),(0,-1),(0,1))
shark_dt = list(map(lambda x: int(x)-1, input().split()))           # 상어별 방향
shark_dts = [[[] for _ in range(M)] for _ in range(4)]              # 상어별 방향 우선순위

for m in range(M):
    for i in range(4):
        shark_dts[i][m] = list(map(lambda x: int(x)-1, input().split()))

time = 0
while True:
    time += 1
    if time > 1000:
        print(-1)
        break

    for m in range(M):
        if len(shark[m]) > K:
            r, c = shark[m].pop(0)
            if (r,c) == (-1,-1): continue
            smell[r][c].pop(0)

    new_matrix = [[row[:] for row in arr[:]] for arr in smell]

    for m in range(M):
        if dead[m]:
            shark[m].append((-1,-1))
            continue

        mine = None
        r, c = shark[m][-1]
        d = shark_dt[m]
        dr = shark_dts[d][m]
        directions = list(map(lambda x: dt[x], dr))

        for i in range(4):
            dx, dy = directions[i]
            nx, ny = r+dx, c+dy

            if not (0 <= nx < N and 0 <= ny < N): continue

            # 아무 냄새가 없으면 간다
            elif not smell[nx][ny]:
                shark_dt[m] = dr[i]
                # 근데 거기 상어가 들어가 있으면
                if new_matrix[nx][ny] and new_matrix[nx][ny][-1] < m:
                    # 죽는다
                    dead[m] = True
                    shark[m].append((-1,-1))
                else:
                    new_matrix[nx][ny].append(m)
                    shark[m].append((nx,ny))
                    shark_dt[m] = dr[i]
                break

            # 냄새가 자기 냄새가 있으면
            elif m in smell[nx][ny]:
                if not mine:
                    mine = [nx,ny,i]
        else:
            if mine:
                # 간다
                nx, ny, i = mine
                new_matrix[nx][ny].append(m)
                shark[m].append((nx,ny))
                shark_dt[m] = dr[i]

    if all(dead[1:]):
        print(time)
        break

    smell = new_matrix