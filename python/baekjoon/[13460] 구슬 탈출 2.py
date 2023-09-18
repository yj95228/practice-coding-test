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