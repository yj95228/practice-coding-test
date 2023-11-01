# https://www.acmicpc.net/problem/16930
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
V = [[-1]*M for _ in range(N)]
V[sr][sc] = 1
queue = deque([(sr, sc)])
while queue:
    r, c = queue.popleft()
    if (r, c) == (er, ec):
        print(V[er][ec]-1)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        for s in range(1, K+1):
            nx, ny = r+s*dx, c+s*dy
            if 0 <= nx < N and 0 <= ny < M:
                if A[nx][ny] == '#': break
                elif -1 != V[nx][ny] <= V[r][c]: break
                elif V[nx][ny] == -1 or V[r][c]+1 < V[nx][ny]:
                    V[nx][ny] = V[r][c]+1
                    queue.append((nx, ny))
            else: break
else: print(-1)