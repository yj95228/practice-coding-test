import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = set()
queue = []
cnt = 0
for r in range(N):
    for c in range(M):
        if A[r][c] == 'o':
            V.add((r, c))
            queue.append((r, c))
            cnt += 1

for _ in range(int(input())):
    next_q = []
    for r, c in queue:
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = r + dx, c + dy
            if (nx, ny) in V: continue
            V.add((nx, ny))
            next_q.append((nx, ny))
            cnt += 1
    queue = next_q
print(cnt)