import sys
input = sys.stdin.readline

def solve():
    V = [[-1] * N for _ in range(N)]
    V[sr][sc] = H
    queue = [(H, 0, sr, sc)]
    turn = 0
    while queue:
        next_q = []
        for h, u, r, c in queue:
            if (r, c) == (er, ec): return turn
            if not h+u: continue
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if A[nx][ny] == '.':
                        if V[nx][ny] < h+u-1:
                            V[nx][ny] = h+u-1
                            if u: next_q.append((h, u-1, nx, ny))
                            else: next_q.append((h-1, u, nx, ny))
                    elif A[nx][ny] == 'U':
                        if V[nx][ny] < h+D if D else h+D-1:
                            V[nx][ny] = h+D if D else h+D-1
                            if u: next_q.append((h, D, nx, ny))
                            else: next_q.append((h-1, D, nx, ny))
        queue = next_q
        turn += 1
    return -1

N, H, D = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc, er, ec = -1, -1, -1, -1
for r in range(N):
    for c in range(N):
        if A[r][c] == 'S':
            sr, sc = r, c
            A[r][c] = '.'
        elif A[r][c] == 'E':
            er, ec = r, c
            A[r][c] = '.'
print(solve())