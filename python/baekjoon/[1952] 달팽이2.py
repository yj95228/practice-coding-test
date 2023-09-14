import sys
input = sys.stdin.readline

M, N = map(int, input().split())
visited = [[False]*N for _ in range(M)]
dt = ((0,1),(1,0),(0,-1),(-1,0))
answer, r, c, d = 0, 0, 0, 0
visited[0][0] = True
for _ in range(M*N-1):
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    if not (0 <= nx < M and 0 <= ny < N) or visited[nx][ny]:
        d = (d+1)%4
        answer += 1
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
    visited[nx][ny] = True
    r, c = nx, ny
print(answer)