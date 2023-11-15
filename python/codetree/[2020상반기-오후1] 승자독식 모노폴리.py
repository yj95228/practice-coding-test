import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(lambda x: int(x)-1, input().split()))
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
player = [[] for _ in range(M)]
dead = [0]*M
for r in range(N):
    for c in range(N):
        if A[r][c]:
            player[A[r][c]-1] = [r, c, arr[A[r][c]-1]]
            smell[r][c] = [A[r][c], K+1]

dt = ((-1,0),(1,0),(0,-1),(0,1))
dd = ['^','v','<','>']
dts = [[list(map(lambda x: int(x)-1, input().split())) for _ in range(4)] for _ in range(M)]

for turn in range(1, 1001):
    B = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if smell[r][c][1]:
                smell[r][c][1] -= 1
                if smell[r][c][1] == 0:
                    smell[r][c][0] = 0

    move = []
    for m, (r, c, d) in enumerate(player):
        if dead[m]: continue
        for i in range(4):
            nd = dts[m][d][i]
            dx, dy = dt[nd]
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not smell[nx][ny][0]:
                move.append((m+1, nx, ny))
                player[m] = [nx, ny, nd]
                break
        else:
            for i in range(4):
                nd = dts[m][d][i]
                dx, dy = dt[nd]
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < N and smell[nx][ny][0] == m+1:
                    move.append((m+1, nx, ny))
                    player[m] = [nx, ny, nd]
                    break

    for idx, r, c in move:
        if B[r][c]:
            dead[idx-1] = 1
        else:
            B[r][c] = idx
            smell[r][c] = [idx, K + 1]

    if all(dead[1:]):
        print(turn)
        break
else: print(-1)