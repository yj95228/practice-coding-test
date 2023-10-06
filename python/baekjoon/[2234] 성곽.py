'''
- 1차. 50% 틀렸습니다
- 2차. (0,0)에서만 연결된 곳 확인하지 말고 모든 곳에서 확인해봐야 함
'''
from sys import stdin
from collections import deque
input = stdin.readline

def dfs1(x,y,group):
    stack = [(x,y)]
    groups[x][y] = group
    cnt = 1
    while stack:
        r, c = stack.pop()
        for i, (dx, dy) in enumerate(((0,1),(1,0),(0,-1),(-1,0))):
            nx, ny = r+dx, c+dy
            if 0 <= nx < M and 0 <= ny < N and not groups[nx][ny]\
            and not matrix[nx][ny] & (1 << i):
                groups[nx][ny] = group
                cnt += 1
                stack.append((nx,ny))
    return cnt

def dfs2(x,y):
    visited = [[0]*N for _ in range(M)]
    visited[x][y] = True
    stack = [(x,y,groups[x][y])]
    while stack:
        r, c, g = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                ng = groups[nx][ny]
                graph[g].add(ng)
                graph[ng].add(g)
                stack.append((nx,ny,ng))

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
groups = [[0]*N for _ in range(M)]
group, answer1, answer2 = 1, 0, 0
cnts = [0]
for r in range(M):
    for c in range(N):
        if not groups[r][c]:
            cnt = dfs1(r,c,group)
            cnts.append(cnt)
            answer1 = max(answer1, cnt)
            group += 1

graph = [set() for _ in range(group)]
for r in range(M):
    for c in range(N):
        dfs2(r,c)
for g in range(1,group):
    for x in graph[g]:
        if x == g: continue
        answer2 = max(answer2, cnts[g]+cnts[x])
print(group-1, answer1, answer2, sep='\n')