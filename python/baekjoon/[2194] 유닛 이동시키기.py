import sys
input = sys.stdin.readline

def solve():
    V = [[0]*M for _ in range(N)]
    V[sr][sc] = 1
    queue = [(sr, sc)]
    turn = 0
    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec): return turn
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny] and not A[nx][ny]:
                    for rr in range(P):
                        flag = False
                        for cc in range(Q):
                            nnx, nny = nx+rr, ny+cc
                            if 0 <= nnx < N and 0 <= nny < M and not A[nnx][nny]:
                                continue
                            else: flag = True; break
                        if flag: break
                    else:
                        V[nx][ny] = 1
                        next_q.append((nx, ny))
        queue = next_q
        turn += 1
    return -1

N, M, P, Q, K = map(int, input().split())
A = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    A[r][c] = 1
sr, sc = map(lambda x: int(x)-1, input().split())
er, ec = map(lambda x: int(x)-1, input().split())
print(solve())