import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
arr = [(N-1, 0),(N-1, 1),(N-2, 0),(N-2, 1)]
dt = ((0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1))
for _ in range(M):
    d, p = map(int, input().split())
    dx, dy = dt[d-1]
    narr = []
    for r, c in arr:
        nx, ny = (r+p*dx)%N, (c+p*dy)%N
        narr.append((nx, ny))
        A[nx][ny] += 1

    B = [row[:] for row in A]
    for r, c in narr:
        for dx, dy in ((1,1),(1,-1),(-1,1),(-1,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny]:
                B[r][c] += 1

    arr = []
    for r in range(N):
        for c in range(N):
            if B[r][c] >= 2:
                if (r, c) in narr: continue
                B[r][c] -= 2
                arr.append((r, c))
    A = B
print(sum([sum(row) for row in A]))