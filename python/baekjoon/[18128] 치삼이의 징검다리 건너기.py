import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, W = map(int, input().split())
D = [[0]*N for _ in range(N)]
queue = []
parents = [x for x in range(N*N)]
for _ in range(W):
    a, b = map(lambda x: int(x)-1, input().split())
    queue.append((a, b))
A = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0
D = [[0]*N for _ in range(N)]
for r, c in queue:
    D[r][c] = 1

day = 2
while queue:
    next_q = []
    for r, c in queue:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not D[nx][ny]:
                D[nx][ny] = day
                next_q.append((nx, ny))
    queue = next_q
    day += 1
D[0][0] = D[N-1][N-1] = 0

V = [[0]*N for _ in range(N)]
queue = [(D[0][0], 0, 0)]
V[0][0] = 1
while queue:
    day, r, c = heappop(queue)
    if (r, c) == (N-1, N-1):
        print(day-1)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and A[nx][ny]:
            V[nx][ny] = 1
            heappush(queue, (max(day, D[nx][ny]), nx, ny))
else: print(-1)