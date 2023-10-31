# https://www.acmicpc.net/problem/14947
from sys import stdin
input = stdin.readline

def solve():
    queue = [(NOPI, [(sr, sc)])]
    time = 0
    while queue:
        temp_q = []
        for box, where in queue:
            if (er, ec) in where:
                return time
            if box == NOPI:
                r, c = where[0]
                for dx, dy in ((0,1),(0,-1)):
                    tmp = []
                    nx1, ny1 = r+dx, c+dy
                    tmp.append((nx1, ny1))
                    nx2, ny2 = nx1+dx, ny1+dy
                    tmp.append((nx2, ny2))
                    nx3, ny3 = nx2+dx, ny2+dy
                    if A[nx2][ny2] or (A[nx1][ny1] and A[nx3][ny3]):
                        mn = min(ny1, ny3)
                        if V[GARO][r][mn]: continue
                        V[GARO][r][mn] = 1
                        tmp.append((nx3, ny3))
                        temp_q.append((GARO, tmp))
                for dx, dy in ((1,0),(-1,0)):
                    tmp = []
                    nx1, ny1 = r+dx, c+dy
                    tmp.append((nx1, ny1))
                    nx2, ny2 = nx1+dx, ny1+dy
                    tmp.append((nx2, ny2))
                    nx3, ny3 = nx2+dx, ny2+dy
                    if A[nx2][ny2] or (A[nx1][ny1] and A[nx3][ny3]):
                        mn = min(nx1, nx3)
                        if V[SERO][mn][c]: continue
                        V[SERO][mn][c] = 1
                        tmp.append((nx3, ny3))
                        temp_q.append((SERO, tmp))
            elif box == GARO:
                rr, mn, mx = None, M+2, 0
                for r, c in where:
                    mn = min(c, mn)
                    mx = max(c, mx)
                    rr = r
                md = (mn+mx)//2
                if A[rr][mn-1]:
                    if not V[NOPI][rr][mn-1]:
                        V[NOPI][rr][mn-1] = 1
                        temp_q.append((NOPI, [(rr, mn-1)]))
                if A[rr][mx+1]:
                    if not V[NOPI][rr][mx+1]:
                        V[NOPI][rr][mx+1] = 1
                        temp_q.append((NOPI, [(rr, mx+1)]))
                for dx in (1,-1):
                    nr = rr+dx
                    if A[nr][md] or (A[nr][mn] and A[nr][mx]):
                        if V[GARO][nr][mn]: continue
                        V[GARO][nr][mn] = 1
                        temp_q.append((GARO, [(nr, mn), (nr, md), (nr, mx)]))
            elif box == SERO:
                cc, mn, mx = None, N+2, 0
                for r, c in where:
                    mn = min(r, mn)
                    mx = max(r, mx)
                    cc = c
                md = (mn+mx)//2
                if A[mn-1][cc]:
                    if not V[NOPI][mn-1][cc]:
                        V[NOPI][mn-1][cc] = 1
                        temp_q.append((NOPI, [(mn-1, cc)]))
                if A[mx+1][cc]:
                    if not V[NOPI][mx+1][cc]:
                        V[NOPI][mx+1][cc] = 1
                        temp_q.append((NOPI, [(mx+1, cc)]))
                for dy in (1,-1):
                    nc = cc+dy
                    if A[md][nc] or (A[mn][nc] and A[mx][nc]):
                        if V[SERO][mn][nc]: continue
                        V[SERO][mn][nc] = 1
                        temp_q.append((SERO, [(mn, nc), (md, nc), (mx,nc)]))

        queue = temp_q
        time += 1
    return -2

N, M = map(int, input().split())
A = [[0]*(M+6) for _ in range(3)] + [[0]*3 + list(map(int, input().rstrip())) + [0]*3 for _ in range(N)] + [[0]*(M+6) for _ in range(3)]
V = [[[0]*(M+6) for _ in range(N+6)] for _ in range(3)]
NOPI, GARO, SERO = 0, 1, 2
sr, sc, er, ec = None, None, None, None
for r in range(3, N+3):
    for c in range(3, M+3):
        if A[r][c] == 2:
            sr, sc = r, c
            A[r][c] = 1
            V[NOPI][r][c] = 1
        elif A[r][c] == 3:
            er, ec = r, c
            A[r][c] = 1
print(solve())