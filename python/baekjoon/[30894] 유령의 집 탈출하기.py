import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [[row[:] for row in A] for _ in range(4)]
dt = ((0,1),(1,0),(0,-1),(-1,0))
for r in range(N):
    for c in range(M):
        if A[r][c].isdigit():
            dd = int(A[r][c])
            for d, (dx, dy) in enumerate(((0,1),(1,0),(0,-1),(-1,0))):
                k = 1
                while True:
                    nx, ny = r+k*dx, c+k*dy
                    if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
                        B[(d-dd)%4][nx][ny] = '#'
                        k += 1
                    else: break
def solve():
    queue = [(sr, sc)]
    V = [[[0]*M for _ in range(N)] for _ in range(4)]
    V[0][sr][sc] = 1
    turn = 0
    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec): return turn
            for dx, dy in ((0,0),(1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and not V[(turn+1)%4][nx][ny] and B[(turn+1)%4][nx][ny] == '.':
                    V[(turn+1)%4][nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
        turn += 1
    return 'GG'

print(solve())