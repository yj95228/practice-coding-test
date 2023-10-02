# 1차 제출: 오전에 못 풀고 점심시간에 풀고 저녁시간에 제출 (거의 4시간 소요)
# 2차 제출: 오전에 풀 때 자꾸 갔던곳 다시 가서 visited 만들어줬었는데 그냥 내가 잘 못 짠거였어서 visited 필요없다는 걸 깨달음
# 3차 제출: 구멍으로 빠지면 바로 리턴하지 않고 다음 방향 보게 했어야 함!!! + 방향을 기억해서 90도만 꺾게 코드 바꿈
import sys
input = sys.stdin.readline

def recur(n, matrix, rx, ry, bx, by, d):
    global answer
    if n > answer:
        return
    elif n > 10:
        return

    for dd in range(4):
        if d == dd or d == (dd+2)%4: continue
        dx, dy = dt[min(3, dd)]
        new_matrix = [row[:] for row in matrix]
        red_hole, blue_hole = False, False
        if rx*dx > bx*dx or ry*dy > by*dy:
            # 빨간색부터
            i = 1
            rnx, rny = rx+i*dx, ry+i*dy
            if new_matrix[rnx][rny] == '#' or new_matrix[rnx][rny] == 'B':
                rnx, rny = rx, ry
            elif new_matrix[rnx][rny] == 'O':
                new_matrix[rx][ry] = '.'
                red_hole = True
            elif new_matrix[rnx][rny] == '.':
                while new_matrix[rnx][rny] == '.':
                    if new_matrix[rnx+dx][rny+dy] != '.': break
                    i += 1
                    rnx, rny = rx+i*dx, ry+i*dy
                if new_matrix[rnx+dx][rny+dy] == 'O':
                    new_matrix[rx][ry] = '.'
                    red_hole = True
                elif new_matrix[rnx+dx][rny+dy] == '#' or new_matrix[rnx+dx][rny+dy] == 'B':
                    new_matrix[rnx][rny] = 'R'
                    new_matrix[rx][ry] = '.'

            # 파란색
            i = 1
            bnx, bny = bx+i*dx, by+i*dy
            if new_matrix[bnx][bny] == '#' or new_matrix[bnx][bny] == 'R':
                bnx, bny = bx, by
            elif new_matrix[bnx][bny] == 'O':
                new_matrix[bx][by] = '.'
                blue_hole = True
            elif new_matrix[bnx][bny] == '.':
                while new_matrix[bnx][bny] == '.':
                    if new_matrix[bnx+dx][bny+dy] != '.': break
                    i += 1
                    bnx, bny = bx+i*dx, by+i*dy
                if new_matrix[bnx+dx][bny+dy] == 'O':
                    new_matrix[bx][by] = '.'
                    blue_hole = True
                elif new_matrix[bnx+dx][bny+dy] == '#' or new_matrix[bnx+dx][bny+dy] == 'R':
                    new_matrix[bnx][bny] = 'B'
                    new_matrix[bx][by] = '.'

        else:
            # 파란색부터
            i = 1
            bnx, bny = bx+i*dx, by+i*dy
            if new_matrix[bnx][bny] == '#' or new_matrix[bnx][bny] == 'R':
                bnx, bny = bx, by
            elif new_matrix[bnx][bny] == 'O':
                new_matrix[bx][by] = '.'
                blue_hole = True
            elif new_matrix[bnx][bny] == '.':
                while new_matrix[bnx][bny] == '.':
                    if new_matrix[bnx+dx][bny+dy] != '.': break
                    i += 1
                    bnx, bny = bx+i*dx, by+i*dy
                if new_matrix[bnx+dx][bny+dy] == 'O':
                    new_matrix[bx][by] = '.'
                    blue_hole = True
                elif new_matrix[bnx+dx][bny+dy] == '#' or new_matrix[bnx+dx][bny+dy] == 'R':
                    new_matrix[bnx][bny] = 'B'
                    new_matrix[bx][by] = '.'

            # 빨간색
            i = 1
            rnx, rny = rx+i*dx, ry+i*dy
            if new_matrix[rnx][rny] == '#' or new_matrix[rnx][rny] == 'B':
                rnx, rny = rx, ry
            elif new_matrix[rnx][rny] == 'O':
                new_matrix[rx][ry] = '.'
                red_hole = True
            elif new_matrix[rnx][rny] == '.':
                while new_matrix[rnx][rny] == '.':
                    if new_matrix[rnx+dx][rny+dy] != '.': break
                    i += 1
                    rnx, rny = rx+i*dx, ry+i*dy
                if new_matrix[rnx+dx][rny+dy] == 'O':
                    new_matrix[rx][ry] = '.'
                    red_hole = True
                elif new_matrix[rnx+dx][rny+dy] == '#' or new_matrix[rnx+dx][rny+dy] == 'B':
                    new_matrix[rnx][rny] = 'R'
                    new_matrix[rx][ry] = '.'

        if blue_hole:
            continue
        elif red_hole:
            answer = min(answer, n)
            continue
        elif not ((rnx, rny) == (rx, ry) and (bnx, bny) == (bx, by)):
            recur(n+1, new_matrix, rnx, rny, bnx, bny, dd)


N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
dt = ((1,0),(0,1),(-1,0),(0,-1))
rx, ry, bx, by, ox, oy = 0, 0, 0, 0, 0, 0
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'R':
            rx, ry = r, c
        elif matrix[r][c] == 'B':
            bx, by = r, c
        elif matrix[r][c] == 'O':
            ox, oy = r, c

dt = ((1,0),(0,1),(-1,0),(0,-1))
answer = 987654321
recur(1, matrix, rx, ry, bx, by, 4)
print(-1 if answer == 987654321 else answer)

# 두번째 풀이
'''
- 재귀 돌릴 때 방문 복구 안 시킴
- 또 구조화 못 시키고 반복문 씀
'''
from sys import stdin
input = stdin.readline

def move(r,c,d, matrix):
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    while matrix[nx][ny] == '.':
        matrix[nx][ny], matrix[r][c] = matrix[r][c], matrix[nx][ny]
        r, c = nx, ny
        nx, ny = r+dx, c+dy
    if matrix[nx][ny] == 'O':
        matrix[r][c] = '.'
        r, c = nx, ny
        return matrix, r, c, True
    return matrix, r, c, False

def recur(n, rr, rc, br, bc, matrix):
    global answer
    if n > 10 or n >= answer: return

    # 왼쪽으로 움직일 때 빨간 공이 더 왼쪽에 있으면
    if rc <= bc:
        narr, nrr, nrc, o_red = move(rr, rc, 0, [row[:] for row in matrix])
        narr, nbr, nbc, o_blue = move(br, bc, 0, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    else:
        narr, nbr, nbc, o_blue = move(br, bc, 0, [row[:] for row in matrix])
        narr, nrr, nrc, o_red = move(rr, rc, 0, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    # 위로 움직일 때 빨간 공이 더 위에 있으면
    if rr <= br:
        narr, nrr, nrc, o_red = move(rr, rc, 1, [row[:] for row in matrix])
        narr, nbr, nbc, o_blue = move(br, bc, 1, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    else:
        narr, nbr, nbc, o_blue = move(br, bc, 1, [row[:] for row in matrix])
        narr, nrr, nrc, o_red = move(rr, rc, 1, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    # 오른쪽으로 움직일 때 빨간 공이 더 오른쪽에 있으면
    if rc >= bc:
        narr, nrr, nrc, o_red = move(rr, rc, 2, [row[:] for row in matrix])
        narr, nbr, nbc, o_blue = move(br, bc, 2, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    else:
        narr, nbr, nbc, o_blue = move(br, bc, 2, [row[:] for row in matrix])
        narr, nrr, nrc, o_red = move(rr, rc, 2, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    # 아래로 움직일 때 빨간 공이 더 밑에 있으면
    if rr >= br:
        narr, nrr, nrc, o_red = move(rr, rc, 3, [row[:] for row in matrix])
        narr, nbr, nbc, o_blue = move(br, bc, 3, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))

    else:
        narr, nbr, nbc, o_blue = move(br, bc, 3, [row[:] for row in matrix])
        narr, nrr, nrc, o_red = move(rr, rc, 3, narr)

        if o_red and not o_blue:
            answer = min(answer, n)
            return
        elif not o_red and not o_blue and (nrr,nrc,nbr,nbc) not in visited:
            visited.add((nrr,nrc,nbr,nbc))
            recur(n+1, nrr, nrc, nbr, nbc, narr)
            visited.remove((nrr,nrc,nbr,nbc))


N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
dt = ((0,-1),(-1,0),(0,1),(1,0))
visited = set()
rr, rc, br, bc = None, None, None, None
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'R':
            rr, rc = r, c
        elif matrix[r][c] == 'B':
            br, bc = r, c
visited.add((rr,rc,br,bc))
answer = 987654321
recur(1, rr, rc, br, bc, matrix)
print(-1 if answer == 987654321 else answer)