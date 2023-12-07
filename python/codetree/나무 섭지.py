def solve(queue):
    time = 0
    while queue:
        next_q = []
        for who, r, c in queue:
            if who == 'G':
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < M and time+1 < G[nx][ny]:
                        G[nx][ny] = time+1
                        next_q.append((who, nx, ny))
            elif who == 'N':
                if (r, c) == (er, ec): return 'Yes'
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < M and time+1 < V[nx][ny] and time+1 < G[nx][ny] and A[nx][ny] == '.':
                        V[nx][ny] = time+1
                        next_q.append((who, nx, ny))
        queue = next_q
        time += 1
    return 'No'


N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc, er, ec = -1, -1, -1, -1
G = [[987654321]*M for _ in range(N)]
V = [[987654321]*M for _ in range(N)]
queue = []
for r in range(N):
    for c in range(M):
        if A[r][c] == 'N':
            sr, sc = r, c
            A[r][c] = '.'
        elif A[r][c] == 'D':
            er, ec = r, c
            A[r][c] = '.'
        elif A[r][c] == 'G':
            queue.append(('G', r, c))
            G[r][c] = 0
queue.append(('N', sr, sc))
V[sr][sc] = 0
print(solve(queue))