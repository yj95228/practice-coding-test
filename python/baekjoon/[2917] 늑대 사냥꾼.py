import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
D = [[0]*M for _ in range(N)]
queue = []
sr, sc, er, ec = None, None, None, None
for r in range(N):
    for c in range(M):
        if A[r][c] == '+':
            queue.append((r, c))
            D[r][c] = -1
        elif A[r][c] == 'V':
            A[r][c] = '.'
            sr, sc = r, c
        elif A[r][c] == 'J':
            A[r][c] = '.'
            er, ec = r, c
while queue:
    next_q = []
    for r, c in queue:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M:
                if D[nx][ny]: continue
                D[nx][ny] = D[r][c] - 1
                next_q.append((nx, ny))
    queue = next_q

answer = D[sr][sc]+1
V = [[987654321] * M for _ in range(N)]
queue = [(D[sr][sc]+1, 1, sr, sc)]
V[sr][sc] = 0
while queue:
    far, dist, r, c = heappop(queue)
    if (r, c) == (er, ec):
        print(-far)
        break
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = r + dx, c + dy
        if 0 <= nx < N and 0 <= ny < M and dist+1 < V[nx][ny]:
            V[nx][ny] = dist+1
            heappush(queue, (max(far, D[nx][ny]+1), dist+1, nx, ny))