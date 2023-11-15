N, M, K = map(int, input().split())
# ↑, ↗, →, ↘, ↓, ↙, ←, ↖
dt = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
A = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    A[x-1][y-1].append((m, s, d))

for _ in range(K):
    crash = set()
    B = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not A[r][c]: continue
            for m, s, d in A[r][c]:
                dx, dy = dt[d]
                nx, ny = (r+s*dx)%N, (c+s*dy)%N
                B[nx][ny].append((m, s, d))
                if len(B[nx][ny]) > 1: crash.add((nx, ny))

    for r, c in crash:
        nm = sum([x[0] for x in B[r][c]])//5
        if nm:
            dd = [x[2]%2 for x in B[r][c]]
            nd = [0,2,4,6] if all(dd) or not any(dd) else [1,3,5,7]
            ns = sum([x[1] for x in B[r][c]])//len(B[r][c])
            B[r][c] = [(nm, ns, d) for d in nd]
        else:
            B[r][c] = []
    A = B

print(sum([x[0] for row in A for xx in row for x in xx]))