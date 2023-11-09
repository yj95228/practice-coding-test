import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0] * M for _ in range(N)]
queue = []
for r in range(N):
    for c in range(M):
        if A[r][c] != '.':
            A[r][c] = int(A[r][c])
            sand = A[r][c]
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
                    V[r][c] += 1
            if sand <= V[r][c]:
                queue.append((r, c))

wave = 0
while queue:
    next_q = []
    for r, c in queue:
        A[r][c] = '.'
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] != '.' and V[nx][ny] < A[nx][ny]:
                V[nx][ny] += 1
                if V[nx][ny] >= A[nx][ny]:
                    next_q.append((nx, ny))

    if next_q:
        wave += 1
        queue = next_q
    else:
        print(wave + 1)
        break

else:
    print(wave)