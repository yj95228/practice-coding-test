import sys
input = sys.stdin.readline

def bfs(x, y):
    arr = [(x, y)]
    queue = [(x, y)]
    V[x][y] = 1
    while queue:
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny] and A[nx][ny]:
                    V[nx][ny] = 1
                    arr.append((nx, ny))
                    next_q.append((nx, ny))
        queue = next_q
    return arr

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
time = 0
while True:
    V = [[0]*M for _ in range(N)]
    P, Q = [], []
    for r in range(N):
        for c in range(M):
            if not V[r][c] and A[r][c]:
                Q.append(bfs(r, c))
    if len(Q) == 1:
        print(time)
        break
    else:
        B = [row[:] for row in A]
        for i, arr in enumerate(Q):
            for r, c in arr:
                num = A[r][c]
                for dx in range(-num, num+1):
                    for dy in range(-num, num+1):
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            V[nx][ny] = 1
                            B[nx][ny] = max(B[nx][ny], num)
        A = B
        time += 1