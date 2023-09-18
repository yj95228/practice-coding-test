import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,land):
    visited[x][y] = land
    queue = deque([(x,y)])
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if new_matrix[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = land
                queue.append((nx,ny))

N, M = map(int, input().split())
matrix = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)]
year = 1

while True:
    new_matrix = [row[:] for row in matrix]
    for r in range(1,N+1):
        for c in range(1,M+1):
            if matrix[r][c]:
                sea = 0
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if not matrix[nx][ny]:
                        sea += 1
                new_matrix[r][c] = max(0, new_matrix[r][c]-sea)

    land = 0
    visited = [[0]*(M+2) for _ in range(N+2)]
    for r in range(1,N+1):
        for c in range(1,M+1):
            if new_matrix[r][c] and not visited[r][c]:
                land += 1
                bfs(r,c,land)

    if land == 0:
        print(0)
        break
    elif land >= 2:
        print(year)
        break

    matrix = new_matrix
    year += 1