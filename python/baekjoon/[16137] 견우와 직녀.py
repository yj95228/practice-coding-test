import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dt = ([(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)])

V = [[[987654321]*N for _ in range(N)] for _ in range(2)]
queue = deque([(0, 0, 0, 0)])
V[0][0][0] = 0
while queue:
    wall, time, r, c = queue.popleft()
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N:
            if A[nx][ny] == 1:
                if time+1 < V[wall][nx][ny]:
                    V[wall][nx][ny] = time+1
                    queue.append((wall, time+1, nx, ny))
            elif not A[nx][ny] and A[r][c] == 1:
                if wall: continue
                wait = (time + M) // M * M - time
                wait = wait if wait else M
                if time + wait < V[wall][nx][ny]:
                    V[wall][nx][ny] = time + wait
                    queue.append((1, time + wait, nx, ny))
            elif A[nx][ny] and A[r][c] == 1:
                wait = (time + A[nx][ny]) // A[nx][ny] * A[nx][ny] - time
                wait = wait if wait else A[nx][ny]
                if time + wait < V[wall][nx][ny]:
                    V[wall][nx][ny] = time + wait
                    queue.append((wall, time + wait, nx, ny))
print(min(V[0][N-1][N-1], V[1][N-1][N-1]))