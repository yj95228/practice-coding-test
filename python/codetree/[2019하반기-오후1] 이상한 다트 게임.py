from collections import deque

def dfs(x, y):
    V[x][y] = 1
    stack = [(x, y, A[x][y])]
    result = [(x, y)]
    while stack:
        r, c, num = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, (c+dy)%M
            if 0 <= nx < N and not V[nx][ny] and A[nx][ny] == num:
                V[nx][ny] = 1
                result.append((nx, ny))
                stack.append((nx, ny, num))

    if len(result) > 1:
        for r, c in result:
            A[r][c] = 0
        return True
    return False

N, M, Q = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(Q):
    x, d, k = map(int, input().split())
    for i in range(x, N+1, x):
        A[i-1].rotate(-k if d else k)

    V = [[0]*M for _ in range(N)]
    erase = False
    cnt, sm = 0, 0
    for r in range(N):
        for c in range(M):
            if not A[r][c]: continue
            elif not V[r][c]:
                if dfs(r, c):
                    erase = True
                else:
                    cnt += 1
                    sm += A[r][c]

    if not erase:
        if not cnt: break
        mean = sm//cnt
        for r in range(N):
            for c in range(M):
                if not A[r][c]: continue
                elif A[r][c] > mean:
                    A[r][c] -= 1
                elif A[r][c] < mean:
                    A[r][c] += 1

print(sum([sum(row) for row in A]))