# https://www.acmicpc.net/problem/1795
from sys import stdin
input = stdin.readline

def bfs(x, y):
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    queue = [(x, y)]
    cnt = 2
    while queue:
        for _ in range(int(A[x][y])):
            temp_q = []
            for r, c in queue:
                for dx, dy in ((1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = cnt
                        temp_q.append((nx, ny))
            queue = temp_q
        cnt += 1
    horse.append(visited)

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
horse = []
idx = 1
for r in range(N):
    for c in range(M):
        if A[r][c] != '.':
            bfs(r, c)
            idx += 1
idx -= 1
answer = 987654321
for r in range(N):
    for c in range(M):
        result = 0
        for h in range(idx):
            if not horse[h][r][c]:
                result = 987654321
                break
            else:
                result += horse[h][r][c]-1
        answer = min(answer, result)
print(-1 if answer == 987654321 else answer)