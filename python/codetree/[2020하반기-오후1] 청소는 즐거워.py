def make_snail():
    sr, sc, sd = N // 2, N // 2, 0
    snails, snail = [(N // 2, N // 2)], 1
    while True:
        for _ in range(2):
            dx, dy = dt[sd]
            for _ in range(1, snail + 1):
                nx, ny = sr + dx, sc + dy
                snails.append((nx, ny))
                if len(snails) == N * N:
                    return snails
                sr, sc = nx, ny
            sd = (sd + 1) % 4
        snail += 1


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dt = ((0, -1), (1, 0), (0, 1), (-1, 0))
snails = make_snail()
sr, sc = N // 2, N // 2
wind = (
    [(5, 0, -2), (10, -1, -1), (10, 1, -1), (7, -1, 0), (7, 1, 0), (2, -2, 0), (2, 2, 0), (1, -1, 1), (1, 1, 1)],
    [(5, 2, 0), (10, 1, -1), (10, 1, 1), (7, 0, -1), (7, 0, 1), (2, 0, -2), (2, 0, 2), (1, -1, -1), (1, -1, 1)],
    [(5, 0, 2), (10, -1, 1), (10, 1, 1), (7, -1, 0), (7, 1, 0), (2, -2, 0), (2, 2, 0), (1, -1, -1), (1, 1, -1)],
    [(5, -2, 0), (10, -1, -1), (10, -1, 1), (7, 0, -1), (7, 0, 1), (2, 0, -2), (2, 0, 2), (1, 1, -1), (1, 1, 1)]
)
answer = 0
for i, (r, c) in enumerate(snails[1:], start=1):
    nx, ny = snails[i - 1]
    ddx, ddy = r - nx, c - ny
    total = A[r][c]
    d = dt.index((ddx, ddy))
    for rate, dx, dy in wind[d]:
        nx, ny = r + dx, c + dy
        dust = A[r][c] * rate // 100
        total -= dust
        if 0 <= nx < N and 0 <= ny < N:
            A[nx][ny] += dust
        else:
            answer += dust
    nx, ny = r + ddx, c + ddy
    if 0 <= nx < N and 0 <= ny < N:
        A[nx][ny] += total
    else:
        answer += total
    A[r][c] = 0

print(answer)