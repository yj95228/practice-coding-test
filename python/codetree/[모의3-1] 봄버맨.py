from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y, n):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    queue = deque([(x,y)])
    cnt = 0
    while queue:
        if cnt == n: break
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        if matrix[nx][ny] == '.':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                        else: return False
                else: return False
        cnt += 1
    return True

def recur(n, r, c):
    global answer
    answer = max(answer, n)
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == '.':
            if bfs(nx, ny, n):
                recur(n+1, nx, ny)

N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
br, bc = None, None
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'B':
            br, bc = r, c
            matrix[r][c] = '.'
answer = 0
recur(1, br, bc)
print(answer)