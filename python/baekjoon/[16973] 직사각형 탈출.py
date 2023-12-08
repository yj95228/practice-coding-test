import sys
input = sys.stdin.readline

def solve():
    V = [[0] * (M+2) for _ in range(N+2)]
    V[sr][sc] = 1
    queue = [(sr, sc)]
    turn = 0
    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec): return turn
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not V[nx][ny] and not B[nx][ny]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
        turn += 1
    return -1

N, M = map(int, input().split())
A = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
H, W, sr, sc, er, ec = map(int, input().split())
B = [[0] * (M+2) for _ in range(N+2)]
for r in range(N+2):
    for c in range(M+2):
        if A[r][c] and not B[r][c]:
            for i in range(H):
                for j in range(W):
                    if 0 <= r-i and 0 <= c-j:
                        B[r-i][c-j] = 1
print(solve())