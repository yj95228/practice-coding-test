# https://www.acmicpc.net/problem/16932
from sys import stdin
input = stdin.readline

def dfs(x, y):
    G[x][y] = idx
    stack = [(x, y)]
    cnt = 1
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and not G[nx][ny] and A[nx][ny]:
                G[nx][ny] = idx
                cnt += 1
                stack.append((nx, ny))
    groups.append(cnt)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
G = [[0]*M for _ in range(N)]
groups = [0]
idx = 1
for r in range(N):
    for c in range(M):
        if A[r][c] and not G[r][c]:
            dfs(r, c)
            idx += 1

answer = 0
for r in range(N):
    for c in range(M):
        if not A[r][c]:
            group = set()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and G[nx][ny]:
                    group.add(G[nx][ny])
            answer = max(answer, sum([groups[g] for g in group])+1)
print(answer)