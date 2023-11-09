N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Y = [[5] * N for _ in range(N)]
V = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    V[r - 1][c - 1].append(age)

for _ in range(K):
    D = [[0] * N for _ in range(N)]
    NV = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not V[r][c]: continue
            V[r][c].sort()
            for virus in V[r][c]:
                if virus <= Y[r][c]:
                    NV[r][c].append(virus + 1)
                    Y[r][c] -= virus
                else:
                    D[r][c] += virus // 2

    for r in range(N):
        for c in range(N):
            Y[r][c] += D[r][c]

    for r in range(N):
        for c in range(N):
            if not NV[r][c]: continue
            for virus in NV[r][c]:
                if virus % 5 == 0:
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            NV[nx][ny].append(1)

    for r in range(N):
        for c in range(N):
            Y[r][c] += A[r][c]

    V = NV

print(sum(len(V[r][c]) for r in range(N) for c in range(N)))