import sys
input = sys.stdin.readline

def dfs(r, c):
    stack = [(r, c)]
    visited = dict()
    visited[(r, c)] = (r, c)
    while stack:
        r, c = stack.pop()
        V[r][c] = 1
        dx, dy = dt[A[r][c]]
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M:
            if visited.get((nx, ny)):
                visited[(nx, ny)] = (r, c)
                arr = []
                x, y = r, c
                while True:
                    if arr and (x, y) == (r, c): break
                    nx, ny = visited.get((r, c))
                    arr.append(B[nx][ny])
                    r, c = nx, ny
                return min(arr)
            else:
                if V[nx][ny]: return 0
                visited[(nx, ny)] = (r, c)
                stack.append((nx, ny))
        else: return 0

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*M for _ in range(N)]
dt = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
answer = 0
for r in range(N):
    for c in range(M):
        if not V[r][c]:
            answer += dfs(r, c)
print(answer)