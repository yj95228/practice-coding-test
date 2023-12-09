import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*M for _ in range(N)]
queue = []
for r in range(N):
    for c in range(M):
        if A[r][c] == 'W':
            queue.append((r, c))
            V[r][c] = 1
while queue:
    next_q = []
    for r, c in queue:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if V[nx][ny]: continue
            if A[nx][ny] == '#': continue
            elif A[nx][ny] == '.':
                V[nx][ny] = 1
                next_q.append((nx, ny))
            else:
                k = 1
                while True:
                    nx, ny = r+k*dx, c+k*dy
                    if A[nx][ny] == '+': k += 1; continue
                    elif A[nx][ny] == '#':
                        nx, ny = r+(k-1)*dx, c+(k-1)*dy
                    if not V[nx][ny]:
                        V[nx][ny] = 1
                        next_q.append((nx, ny))
                    break
    queue = next_q
    
for r in range(N):
    for c in range(M):
        if A[r][c] == '.' and not V[r][c]:
            A[r][c] = 'P'
for row in A:
    print(''.join(row))