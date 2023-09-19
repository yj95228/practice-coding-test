# 1차 제출: 25% 틀렸습니다
# 2차 제출: 목표점에 이미 박스가 있을 수도 있으니 박스 수로 목표점 수를 세는 것으로 변경
# 3차 제출: 목표점에 이미 캐릭터가 있을 수도 있으니 해당 조건 추가
# 4차 제출: 목표점에 이미 캐릭터가 있을 때 . 가 아니라 +로 바꿔줬어야 했음
# 5차 제출: 이거 또 틀리면 w랑 W 지도에 그냥 찍어주는 걸로 바꿔야겠다
# 6차 제출: 빡하드코딩
# 7차 제출: 이미 모든 박스가 목표점에 이동된 경우를 고려하지 않음
# https://www.acmicpc.net/problem/4577
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

game = 1
dt = {'U':(-1,0), 'L':(0,-1), 'R':(0,1), 'D':(1,0)}
while True:
    R, C = map(int, input().split())
    if (R,C) == (0,0): break
    matrix = [list(input().rstrip()) for _ in range(R)]

    sr, sc, target, complete = 0, 0, 0, 0
    for r in range(1,R-1):
        for c in range(1,C-1):
            if matrix[r][c] == '+':
                target += 1
            elif matrix[r][c] == 'w':
                matrix[r][c] = '.'
                sr, sc = r, c
            elif matrix[r][c] == 'W':
                matrix[r][c] = '+'
                sr, sc = r, c
                target += 1
            elif matrix[r][c] == 'B':
                complete += 1

    command = input().rstrip()
    for d in command:
        dx, dy = dt[d]
        nx, ny = sr+dx, sc+dy

        # 캐릭터에게 지시한 방향이 빈 칸(박스나 벽이 아닌 곳)인 경우에는 그 칸으로 이동한다.
        if matrix[nx][ny] == '.' or matrix[nx][ny] == '+': pass
        # 지시한 방향에 박스가 있는 경우에는, 박스를 민다.
        elif matrix[nx][ny] == 'b':
            # 이 경우에는 박스가 이동할 칸도 비어있어야 한다.
            if matrix[nx+dx][ny+dy] == '.':
                matrix[nx][ny], matrix[nx+dx][ny+dy] = '.', 'b'
            elif matrix[nx+dx][ny+dy] == '+':
                matrix[nx][ny], matrix[nx+dx][ny+dy] = '.', 'B'
                complete -= 1
            # 박스가 이동할 칸에 다른 박스나 벽이 있는 경우에는 키를 눌러도 캐릭터는 이동하지 않는다.
            else: continue
        elif matrix[nx][ny] == 'B':
            if matrix[nx+dx][ny+dy] == '.':
                matrix[nx][ny], matrix[nx+dx][ny+dy] = '+', 'b'
                complete += 1
            elif matrix[nx+dx][ny+dy] == '+':
                matrix[nx][ny], matrix[nx+dx][ny+dy] = '+', 'B'
            else: continue
        # 지시한 방향이 벽인 경우,
        else: continue

        sr, sc = nx, ny
        if target == complete: break

    print(f'Game {game}: {"incomplete" if target == complete else "complete"}')
    matrix[sr][sc] = 'W' if matrix[sr][sc] == '+' else 'w'
    for row in matrix:
        print(''.join(row))
    game += 1