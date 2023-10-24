from sys import stdin
from collections import deque
input = stdin.readline

def solve():
    visited = [[0]*C for _ in range(R)]
    visited[sr][sc] = 1
    queue = deque([(sr, sc, x, 0, [row[:] for row in A], [row[:] for row in visited]) for x in range(4)])
    while queue:
        r, c, d, make, B, V = queue.popleft()
        if (r,c) == (er,ec):
            flag = True
            for r in range(R):
                for c in range(C):
                    if B[r][c]:
                        if not V[r][c]: flag = False
                    if not flag: break
                if not flag: break
            if flag:
                for r in range(R):
                    for c in range(C):
                        if A[r][c] != B[r][c]:
                            return r+1, c+1, answer[B[r][c]]
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if 0 <= nx < R and 0 <= ny < C:
            V[nx][ny] = 1
            if B[nx][ny]:
                if d in iin[B[nx][ny]]:
                    queue.append((nx, ny, dts[B[nx][ny]][d], make, [row[:] for row in B], [row[:] for row in V]))
            elif not make:
                for x in range(1,8):
                    B[nx][ny] = x
                    if d in iin[B[nx][ny]]:
                        if dts[x][d] == -1: continue
                        queue.append((nx, ny, dts[B[nx][ny]][d], 1, [row[:] for row in B], [row[:] for row in V]))
                    B[nx][ny] = 0
            V[nx][ny] = 0

R, C = map(int, input().split())
A = [list(input().rstrip()) for _ in range(R)]
sr, sc, er, ec = None, None, None, None
for r in range(R):
    for c in range(C):
        if A[r][c] == 'M':
            A[r][c] = 7
            sr, sc = r, c
        elif A[r][c] == 'Z':
            A[r][c] = 7
            er, ec = r, c
        elif A[r][c] == '|':
            A[r][c] = 5
        elif A[r][c] == '-':
            A[r][c] = 6
        elif A[r][c] == '+':
            A[r][c] = 7
        elif A[r][c] == '.':
            A[r][c] = 0
        else:
            A[r][c] = int(A[r][c])

dt = ((0,1),(1,0),(0,-1),(-1,0))
iin = ([],[2,3],[1,2],[0,1],[0,3],[1,3],[0,2],[0,1,2,3],[0,1,2,3])  # 들어갈수 있는 방향
dts = ([],[-1,-1,1,0],[-1,0,3,-1],[3,2,-1,-1],[1,-1,-1,2],[-1,1,-1,3],[0,-1,2,-1],[0,1,2,3],[0,1,2,3])
answer = [0,1,2,3,4,'|','-','+']
print(*solve())