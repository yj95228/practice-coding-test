import sys
input = sys.stdin.readline

def solve():
    queue = [(sh, sr, sc)]
    V = [[[0]*C for _ in range(R)] for _ in range(L)]
    V[sh][sr][sc] = 1
    while queue:
        next_q = []
        for h, r, c in queue:
            if (h, r, c) == (eh, er, ec):
                return f'Escaped in {V[h][r][c]-1} minute(s).'
            for dx, dy, dz in ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)):
                nx, ny, nz = h+dx, r+dy, c+dz
                if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and not V[nx][ny][nz] and A[nx][ny][nz] == '.':
                    V[nx][ny][nz] = V[h][r][c] + 1
                    next_q.append((nx, ny, nz))
        queue = next_q
    return 'Trapped!'

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0): break
    A = []
    for _ in range(L):
        A.append([list(input().rstrip()) for _ in range(R)])
        input()
    sh, sr, sc, eh, er, ec = None, None, None, None, None, None
    for h in range(L):
        for r in range(R):
            for c in range(C):
                if A[h][r][c] == 'S':
                    sh, sr, sc = h, r, c
                    A[h][r][c] = '.'
                elif A[h][r][c] == 'E':
                    eh, er, ec = h, r, c
                    A[h][r][c] = '.'

    print(solve())