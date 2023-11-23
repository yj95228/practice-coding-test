import sys
input = sys.stdin.readline

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    parents[b] = a
    return True

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def dfs(r, c):
    dx, dy = dt[A[r][c]]
    nx, ny = r+dx, c+dy
    if 0 <= nx < N and 0 <= ny < M:
        if union(r*M+c, nx*M+ny):
            dfs(nx, ny)

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
dt = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
parents = [r*M+c for r in range(N) for c in range(M)]
for r in range(N):
    for c in range(M):
        if parents[r*M+c] == r*M+c:
            dfs(r, c)
answer = 0
for i, x in enumerate(parents):
    if i == x:
        answer += 1
print(answer)