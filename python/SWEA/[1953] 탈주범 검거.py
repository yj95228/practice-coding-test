# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
from collections import deque

def bfs(r, c, l):
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    queue = deque([(r, c, 1, matrix[r][c])])
    cnt = 1
    while queue:
        r, c, time, tunnel = queue.popleft()
        if time == l: break
        for d in go[tunnel]:
            dx, dy = dt[d]
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and d in come[matrix[nx][ny]]:
                visited[nx][ny] = visited[r][c] + 1
                queue.append((nx, ny, time+1, matrix[nx][ny]))
                cnt += 1
    return cnt

T = int(input())
dt = ((1,0),(0,-1),(-1,0),(0,1))    # v < ^ >
come = [[], [0,1,2,3], [0,2], [1,3], [0,1], [1,2], [2,3], [3,0]]
go = [[], [0,1,2,3], [0,2], [1,3], [2,3], [3,0], [0,1], [1,2]]
for tc in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(R, C, L)}')