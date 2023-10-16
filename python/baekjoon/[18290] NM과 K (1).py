# https://www.acmicpc.net/problem/18290

# 첫번째 풀이
from sys import stdin
input = stdin.readline

def recur(n, cnt, result, visited):
    global answer
    if cnt == K:
        answer = max(answer, result)
        return
    if n == N*M: return
    recur(n+1, cnt, result, [row[:] for row in visited])
    r, c = select[n]
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            return
    visited[r][c] = 1
    recur(n+1, cnt+1, result+A[r][c], [row[:] for row in visited])
    visited[r][c] = 0

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
select = []
for r in range(N):
    for c in range(M):
        select.append((r,c))
answer = -10001
recur(0, 0, 0, [[0]*M for _ in range(N)])
print(answer)

# 2번째 풀이
def recur(n, cnt, sm):
    if cnt == K:
        global answer
        answer = max(answer, sm)
        return
    for i in range(n, N*M):
        r, c = i//M, i%M
        flag = True
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                flag = False
                break
        if flag:
            visited[r][c] = 1
            recur(i+1, cnt+1, sm+A[r][c])
            visited[r][c] = 0

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = -10001
recur(0, 0, 0)
print(answer)