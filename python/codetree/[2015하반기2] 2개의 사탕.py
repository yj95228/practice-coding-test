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

# 2차 풀이
from sys import stdin
input = stdin.readline

def solve(rr, rc, br, bc):
    V = set()
    V.add((rr, rc, br, bc))
    turn = 0
    queue = [(rr, rc, br, bc)]
    while queue:
        if turn >= 10: return -1
        next_q = []
        for rr, rc, br, bc in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                red, blue = False, False
                s = 0
                while not red:
                    s += 1
                    nrx, nry = rr+s*dx, rc+s*dy
                    if A[nrx][nry] == 'O':
                        red = True
                    elif (nrx, nry) == (br, bc) or A[nrx][nry] == '#':
                        s -= 1
                        break
                nrr, nrc = rr+s*dx, rc+s*dy
                s = 0
                while not blue:
                    s += 1
                    nbx, nby = br+s*dx, bc+s*dy
                    if A[nbx][nby] == 'O':
                        blue = True
                    elif (nbx, nby) == (nrr, nrc) or A[nbx][nby] == '#':
                        s -= 1
                        break
                nbr, nbc = br+s*dx, bc+s*dy
                s = 0
                while not red:
                    s += 1
                    nrx, nry = nrr+s*dx, nrc+s*dy
                    if A[nrx][nry] == 'O':
                        red = True
                    elif (nrx, nry) == (nbr, nbc) or A[nrx][nry] == '#':
                        s -= 1
                        break
                nrr, nrc = nrr+s*dx, nrc+s*dy
                if red and not blue:
                    return turn+1
                elif not red and not blue and (nrr, nrc, nbr, nbc) not in V:
                    V.add((nrr, nrc, nbr, nbc))
                    next_q.append((nrr, nrc, nbr, nbc))
        turn += 1
        queue = next_q
    return -1

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
rr, rc, br, bc = None, None, None, None
for r in range(N):
    for c in range(M):
        if A[r][c] == 'R':
            rr, rc = r, c
            A[r][c] = '.'
        elif A[r][c] == 'B':
            br, bc = r, c
            A[r][c] = '.'
print(solve(rr, rc, br, bc))