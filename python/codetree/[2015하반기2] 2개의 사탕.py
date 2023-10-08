from sys import stdin
input = stdin.readline

def move(r, c, d, matrix, red=True):
    dx, dy = dt[d]
    goosle = 'B' if red else 'R'
    while True:
        nx, ny = r+dx, c+dy
        if matrix[nx][ny] == '.':
            matrix[r][c], matrix[nx][ny] = matrix[nx][ny], matrix[r][c]
            r, c = nx, ny
        elif matrix[nx][ny] == '#' or matrix[nx][ny] == goosle:
            return matrix, r, c
        elif matrix[nx][ny] == 'O':
            matrix[r][c] = '.'
            return matrix, nx, ny

def recur(n, rr, rc, br, bc, matrix):
    global answer
    if n >= answer or n == 10:
        return
    
    dd = [(rr, br), (br, rr), (rc, bc), (bc, rc)]

    for i in range(4):
        narr = [row[:] for row in matrix]
        xx, yy = dd[i]
        if xx <= yy:
            narr, nrr, nrc = move(rr, rc, i, narr)
            narr, nbr, nbc = move(br, bc, i, narr, False)
        else:
            narr, nbr, nbc = move(br, bc, i, narr, False)
            narr, nrr, nrc = move(rr, rc, i, narr)

        if narr[nbr][nbc] == 'O': continue
        elif narr[nrr][nrc] == 'O':
            answer = min(answer, n+1)
            continue
        elif (nrr, nrc, nbr, nbc) in visited: continue
        else:
            visited.add((nrr, nrc, nbr, nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr, nrc, nbr, nbc))

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
rr, rc, br, bc, er, ec = None, None, None, None, None, None
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'R':
            rr, rc = r, c
        elif matrix[r][c] == 'B':
            br, bc = r, c
        elif matrix[r][c] == 'O':
            er, ec = r, c
answer = 11
dt = ((-1,0),(1,0),(0,-1),(0,1))
visited = set()
visited.add((rr, rc, br, bc))
recur(0, rr, rc, br, bc, matrix)
print(-1 if answer == 11 else answer)