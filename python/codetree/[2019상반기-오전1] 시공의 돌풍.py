N, M, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
r1, r2 = None, None
for r in range(N):
    if A[r][0] == -1:
        r1, r2 = r, r + 1
        break

for _ in range(T):
    B = [row[:] for row in A]
    for r in range(N):
        for c in range(M):
            if A[r][c] < 5: continue
            dirty = A[r][c] // 5
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if ny == 0 and nx in (r1, r2): continue
                    B[nx][ny] += dirty
                    B[r][c] -= dirty

    for r in range(r1 - 1, 0, -1):
        B[r][0] = B[r - 1][0]
    for c in range(M - 1):
        B[0][c] = B[0][c + 1]
    for r in range(r1):
        B[r][M - 1] = B[r + 1][M - 1]
    for c in range(M - 1, 1, -1):
        B[r1][c] = B[r1][c - 1]

    for r in range(r2 + 1, N - 1):
        B[r][0] = B[r + 1][0]
    for c in range(M - 1):
        B[N - 1][c] = B[N - 1][c + 1]
    for r in range(N - 1, r2, -1):
        B[r][M - 1] = B[r - 1][M - 1]
    for c in range(M - 1, 1, -1):
        B[r2][c] = B[r2][c - 1]

    B[r1][1], B[r2][1] = 0, 0
    A = B

print(sum(A[r][c] for r in range(N) for c in range(M) if A[r][c] > 0))