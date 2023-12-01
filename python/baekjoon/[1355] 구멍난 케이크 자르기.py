import sys

input = sys.stdin.readline

LC, LH = map(int, input().split())
H = int(input())
arrh = list(map(int, input().split()))
V = int(input())
arrv = list(map(int, input().split()))

N = 4 * LC - 1
A = [[1] * N for _ in range(N)]
for r in range(4 * LH - 1):
    for c in range(4 * LH - 1):
        A[r + 2 * LC - 2 * LH][c + 2 * LC - 2 * LH] = 0

for h in arrh:
    A[2 * (LC + h) - 1] = [0] * N
A = list(zip(*A))
for v in arrv:
    A[2 * (LC + v) - 1] = [0] * N

visited = [[0] * N for _ in range(N)]
group = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c] and A[r][c]:
            visited[r][c] = group
            queue = [(r, c)]
            while queue:
                next_q = []
                for r, c in queue:
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and A[nx][ny]:
                            visited[nx][ny] = group
                            next_q.append((nx, ny))
                queue = next_q
            group += 1
print(group - 1)