# https://www.codetree.ai/training-field/frequent-problems/problems/rudolph-rebellion/description?page=1&pageSize=20
from sys import stdin
input = stdin.readline

def in_range(r, c):
    return True if 0 <= r < N and 0 <= c < N else False

def find_santa():
    idx, mn, st_r, st_c = None, 987654321, None, None
    for p in range(1, P+1):
        if dead[p]: continue
        sr, sc = santa[p][0], santa[p][1]
        dist = (sr-rr)**2+(sc-rc)**2
        if dist < mn:
            idx, mn, st_r, st_c = p, dist, sr, sc
        elif mn == dist:
            if st_r < sr:
                idx, st_r, st_c = p, sr, sc
            elif st_r == sr:
                if st_c < sc:
                    idx, st_c = p, sc
    return idx

def r_move(idx):
    global rr, rc
    sr, sc = santa[idx][0], santa[idx][1]
    mn, rd = 987654321, None
    for d in range(8):
        dx, dy = dt[d]
        nx, ny = rr+dx, rc+dy
        if in_range(nx, ny):
            dist = (nx-sr)**2+(ny-sc)**2
            if dist < mn:
                mn, rd = dist, d
    dx, dy = dt[rd]
    nx, ny = rr+dx, rc+dy
    rr, rc = nx, ny
    if A[rr][rc]: r_crash(rr, rc, rd)

def r_crash(rr, rc, rd):
    idx = A[rr][rc]
    sr, sc, k, score = santa[idx]
    dx, dy = dt[rd]
    nx, ny = sr+C*dx, sc+C*dy
    santa[idx] = [nx, ny, turn, score+C]
    if in_range(nx, ny):
        if A[nx][ny]:
            dfs(sr, sc, nx, ny, dx, dy)
        else:
            A[sr][sc], A[nx][ny] = A[nx][ny], A[sr][sc]
    else:
        A[sr][sc] = 0
        dead[idx] = 1

def s_crash(idx, sr, sc, sd):
    _, _, k, score = santa[idx]
    dx, dy = dt[sd]
    nx, ny = sr-D*dx, sc-D*dy
    santa[idx] = [nx, ny, turn, score+D]
    if in_range(nx, ny):
        if A[nx][ny]:
            dfs(sr, sc, nx, ny, -dx, -dy)
        else:
            A[sr][sc], A[nx][ny] = A[nx][ny], A[sr][sc]
    else:
        A[sr][sc] = 0
        dead[idx] = 1

def s_move(idx, sr, sc):
    now = (sr-rr)**2+(sc-rc)**2
    sd = None
    for d in range(4):
        dx, dy = dt[d]
        nx, ny = sr+dx, sc+dy
        if in_range(nx, ny):
            dist = (nx-rr)**2+(ny-rc)**2
            if dist < now and not A[nx][ny]:
                now, sd = dist, d
    if sd is None: return
    dx, dy = dt[sd]
    nx, ny = sr+dx, sc+dy
    A[sr][sc], A[nx][ny] = A[nx][ny], A[sr][sc]
    santa[idx][0], santa[idx][1] = nx, ny
    if (nx, ny) == (rr, rc):
        s_crash(idx, nx, ny, sd)

def dfs(sr1, sc1, sr2, sc2, dx, dy):
    stack = [(sr1, sc1), (sr2, sc2)]
    while stack:
        r, c = stack[-1]
        nx, ny = r+dx, c+dy
        if in_range(nx, ny):
            if A[nx][ny]:
                stack.append((nx, ny))
            else:
                idx = A[r][c]
                santa[idx][0], santa[idx][1] = nx, ny
                A[nx][ny], A[r][c] = A[r][c], A[nx][ny]
                while stack:
                    r, c = stack.pop()
                    if stack and stack[-1]:
                        r2, c2 = stack[-1]
                        idx = A[r2][c2]
                        santa[idx][0], santa[idx][1] = r, c
                        A[r][c] = A[r2][c2]
                    else:
                        A[r][c] = 0
                return
        else:
            idx = A[r][c]
            dead[idx] = 1
            A[r][c] = 0
            while stack:
                r, c = stack.pop()
                if stack and stack[-1]:
                    r2, c2 = stack[-1]
                    idx = A[r2][c2]
                    santa[idx][0], santa[idx][1] = r, c
                    A[r][c] = A[r2][c2]
                else:
                    A[r][c] = 0
            return

N, M, P, C, D = map(int, input().split())
dt = ((-1,0),(0,1),(1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
rr, rc = map(lambda x: int(x)-1, input().split())
A = [[0]*N for _ in range(N)]
santa = [[] for _ in range(P+1)]
dead = [0]*(P+1)
for _ in range(P):
    idx, sr, sc = map(lambda x: int(x)-1, input().split())
    santa[idx+1] = [sr, sc, -1, 0]   # 위치, 기절, 점수
    A[sr][sc] = idx+1

for turn in range(1, M+1):
    p = find_santa()
    if p is None: break
    r_move(p)

    # 산타
    for p in range(1, P+1):
        if dead[p]: continue
    # (1) 루돌프 향해 거리 비교 (상우하좌)
        sr, sc, k, score = santa[p]
        if k+2 <= turn:
            s_move(p, sr, sc)

    for p in range(1, P+1):
        if dead[p]: continue
        santa[p][-1] += 1

print(*[s[-1] for s in santa[1:]])

# 2차 풀이
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def calc(r, c, x, y):
    return (r-x)**2+(c-y)**2

def interact(idx, r, c, dx, dy):
    stack = [(idx, r, c)]
    while True:
        p, r, c = stack[-1]
        if A[r][c]:
            nx, ny = r+dx, c+dy
            if in_range(nx, ny):
                stack.append((A[r][c], nx, ny))
            else:
                stack.append((A[r][c], -1, -1))
                break
        else: break
    while stack:
        p, r, c = stack.pop()
        if r == -1:
            state[p][1] = 1
        else:
            santa[p] = [r, c]
            A[r][c] = p

N, M, P, C, D = map(int, input().split())
rr, rc = map(lambda x: int(x)-1, input().split())
A = [[0]*N for _ in range(N)]
santa = [[] for _ in range(P+1)]
state = [[] for _ in range(P+1)]
for _ in range(P):
    p, sr, sc = map(int, input().split())
    A[sr-1][sc-1] = p
    santa[p] = [sr-1, sc-1]             # r, c
    state[p] = [0]*3                    # 기절, 죽음, 점수

for turn in range(1, M+1):
    # 루돌프 움직이기
    # 게임에서 탈락하지 않는 산타 중 가까운 산타 찾기
    mn, mr, mc, midx = 987654321, -1, -1, -1
    for p in range(1, P+1):
        if state[p][1]: continue
        sr, sc = santa[p]
        dist = calc(rr, rc, sr, sc)
        if dist < mn:
            mn, mr, mc, midx = dist, sr, sc, p
        if dist == mn:
            if mr < sr:
                mn, mr, mc, midx = dist, sr, sc, p
            elif mr == sr:
                if mc < sc:
                    mn, mr, mc, midx = dist, sr, sc, p

    # 8방향 중 찾기
    mn, mrr, mrc, mdx, mdy = 987654321, -1, -1, -1, -1
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
        nx, ny = rr+dx, rc+dy
        if in_range(nx, ny):
            dist = calc(nx, ny, mr, mc)
            if dist < mn:
                mn, mrr, mrc, mdx, mdy = dist, nx, ny, dx, dy
    rr, rc = mrr, mrc

    # 산타와 부딪히면 충돌
    if (mr, mc) == (rr, rc):
        A[mr][mc] = 0
        nx, ny = mr+C*mdx, mc+C*mdy
        state[midx][0] = turn+2
        state[midx][2] += C
        if in_range(nx, ny):
            santa[midx] = nx, ny
            if A[nx][ny]:
                interact(midx, nx, ny, mdx, mdy)
            else: A[nx][ny] = midx
        else:
            state[midx][1] = 1

    # 1~P 산타 움직이기
    for p in range(1, P+1):
        if state[p][1]: continue
        elif turn < state[p][0]: continue
        sr, sc = santa[p]
        # 루돌프와 가까워지는 방향 찾아서 움직이기 (다른 산타 있는 곳 X)
        mn, msr, msc, mdx, mdy = calc(sr, sc, rr, rc), -1, -1, -1, -1
        for dx, dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx, ny = sr+dx, sc+dy
            if in_range(nx, ny) and not A[nx][ny]:
                dist = calc(nx, ny, rr, rc)
                if dist < mn:
                    mn, msr, msc, mdx, mdy = dist, nx, ny, dx, dy
        if mn == calc(sr, sc, rr, rc): continue

        if (msr, msc) == (rr, rc):
            A[msr][msc] = 0
            nx, ny = msr-D*mdx, msc-D*mdy
            state[p][0] = turn + 2
            state[p][2] += D
            if in_range(nx, ny):
                A[sr][sc] = 0
                santa[p] = [nx, ny]
                if A[nx][ny] and A[nx][ny] != p:
                    interact(p, nx, ny, -mdx, -mdy)
                else: A[nx][ny] = p
            else:
                state[p][1] = 1
                A[sr][sc] = 0
        elif msr != -1:
            A[sr][sc], A[msr][msc] = A[msr][msc], A[sr][sc]
            santa[p] = [msr, msc]

    flag = False
    for p in range(1, P+1):
        if not state[p][1]:
            flag = True
            state[p][2] += 1
    if not flag: break

print(*[state[p][2] for p in range(1, P+1)])