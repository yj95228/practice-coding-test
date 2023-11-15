def go(sx, sy, ex, ey, C):
    V = [[0]*N for _ in range(N)]
    V[sx][sy] = 1
    queue = [(sx, sy)]
    for oil in range(C+1):
        next_q = []
        for r, c in queue:
            if (r, c) == (ex, ey):
                return ex, ey, C+oil
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and not A[nx][ny]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
    return sx, sy, -1

def bfs(sr, sc, C):
    V = [[0]*N for _ in range(N)]
    V[sr][sc] = 1
    queue = [(sr, sc)]
    for oil in range(C+1):
        next_q = []
        cust = []
        for r, c in queue:
            if customer.get((r, c)):
                cust.append((r, c))
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and not A[nx][ny]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        if cust:
            sx, sy = min(cust)
            ex, ey = customer[(sx, sy)]
            del customer[(sx, sy)]
            if C-oil:
                return go(sx, sy, ex, ey, C-oil)
        queue = next_q
    return sr, sc, -1

N, M, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
sr, sc = map(lambda x: int(x)-1, input().split())
customer = dict()
for _ in range(M):
    sx, sy, ex, ey = map(lambda x: int(x)-1, input().split())
    customer[(sx, sy)] = (ex, ey)

for _ in range(M):
    sr, sc, C = bfs(sr, sc, C)
    if C == -1:
        print(-1)
        break
else: print(C)