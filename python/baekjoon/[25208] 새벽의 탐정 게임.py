import sys
input = sys.stdin.readline

def solve():
    queue = [(sr, sc, dice[:])]
    V[0][sr][sc] = 1
    turn = 0
    while queue:
        next_q = []
        for r, c, dd in queue:
            if (r, c) == (er, ec):
                if dd[0] == 0:
                    return turn
                else: continue
            for d in range(4):
                dx, dy = dt[d]
                nx, ny = r + dx, c + dy
                if A[nx][ny] != '#':
                    new_d = list(map(lambda x: rotate[d][x], dd))
                    if V[new_d[0]][nx][ny]: continue
                    V[new_d[0]][nx][ny] = 1
                    next_q.append((nx, ny, new_d))
        queue = next_q
        turn += 1
    return -1

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[[0]*M for _ in range(N)] for _ in range(6)]
dice = [x for x in range(6)]    # 밑(0), 앞(1), 위(2), 뒤(3), 왼(4), 오(5)
dt = ((-1,0),(1,0),(0,-1),(0,1))
rotate = (
    (3,0,1,2,4,5),
    (1,2,3,0,4,5),
    (4,1,5,3,2,0),
    (5,1,4,3,0,2)
)
sr, sc, er, ec = None, None, None, None
for r in range(1, N-1):
    for c in range(1, M-1):
        if A[r][c] == 'D':
            sr, sc = r, c
            A[r][c] = '.'
        elif A[r][c] == 'R':
            er, ec = r, c
            A[r][c] = '.'
print(solve())