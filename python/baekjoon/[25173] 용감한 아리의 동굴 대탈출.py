# https://www.acmicpc.net/problem/25173
import sys

input = sys.stdin.readline


def bfs(x, y):
    V = [[0] * M for _ in range(N)]
    V[x][y] = 1
    queue = [(x, y)]
    damage = E
    for _ in range(E):
        next_q = []
        for r, c in queue:
            if (r, c) == (sr, sc):
                global A
                A -= damage
                return
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny] and not G[nx][ny] and (nx, ny) != (er, ec):
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
        damage -= 1


def boss(ed):
    cnt, snail = 1, 1
    ed -= 1
    r, c = er, ec
    while True:
        for _ in range(2):
            ed = (ed + 1) % 4
            dx, dy = dt[ed]
            for _ in range(snail):
                if cnt == N * M: return
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < M:
                    cnt += 1
                    if G[nx][ny] == 1:
                        bfs(nx, ny)
                        return
                r, c = nx, ny
        snail += 1


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
A, D, B, E = map(int, input().split())
sr, sc, sd, er, ec, ed = None, None, None, None, None, None
for r in range(N):
    for c in range(M):
        if G[r][c] == 2:
            sr, sc = r, c
            G[r][c] = 0
        elif G[r][c] == 3:
            er, ec = r, c
            G[r][c] = 0
dt = ((0, 1), (1, 0), (0, -1), (-1, 0))
for d, (dx, dy) in enumerate(dt):
    nx, ny = er + dx, ec + dy
    if 0 <= nx < N and 0 <= ny < M and (nx, ny) == (sr, sc):
        sd = ed = d
        break

while True:
    # [1] 아리의 공격
    B -= D
    if B <= 0:
        print('VICTORY!')
        break

    # [2] 아리의 이동
    ssr, ssc = sr, sc
    for d in range(4):
        dx, dy = dt[(sd + d) % 4]
        nx, ny = sr + dx, sc + dy
        if 0 <= nx < N and 0 <= ny < M and not G[nx][ny] and (nx, ny) != (er, ec):
            sr, sc, sd = nx, ny, (sd + d) % 4
            A -= d
            break
    else: A -= 4

    if A <= 0:
        print('CAVELIFE...')
        break

    # [3] 보스의 공격
    boss(ed)

    if A <= 0:
        print('CAVELIFE...')
        break

    # [4] 보스의 이동
    if (ssr, ssc) != (sr, sc):
        ed = sd
        er, ec = ssr, ssc