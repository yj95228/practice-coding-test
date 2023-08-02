# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc
import sys

def shoot(game_map, r, c, x, y):
    for direction, dx, dy in (('^',-1,0),('v',1,0),('<',0,-1),('>',0,1)):
        if game_map[r][c] == direction:
            if 0 <= x+dx < len(game_map) and 0 <= y+dy < len(game_map[0]):
                if game_map[x+dx][y+dy] == '.' or game_map[x+dx][y+dy] == '-':   # 평지 or 물
                    shoot(game_map, r, c, x+dx, y+dy)
                # 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다.
                elif game_map[x+dx][y+dy] == '*': # 벽돌
                    game_map[x+dx][y+dy] = '.'
            return game_map, r, c, x, y

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    r, c, game_map = 0, 0, []
    for x in range(H):
        line = list(input())
        game_map.append(line)
        if '^' in line: r, c = x, line.index('^')
        elif 'v' in line: r, c = x, line.index('v')
        elif '<' in line: r, c = x, line.index('<')
        elif '>' in line: r, c = x, line.index('>')
    _ = int(input())
    command = list(input())
    for x in command:
        if x == 'S':
            game_map, r, c, _, _ = shoot(game_map, r, c, r, c)
        else:
            for command, direction, dx, dy in (('U', '^', -1, 0), ('D', 'v', 1, 0), ('L', '<', 0, -1), ('R', '>', 0, 1)):
                if x == command:
                    game_map[r][c] = direction
                    if 0 <= r + dx < H and 0 <= c + dy < W and game_map[r + dx][c + dy] == '.':
                        game_map[r][c] = '.'
                        game_map[r + dx][c + dy] = direction
                        r, c = r + dx, c + dy
    print(f'#{tc}', end=' ')
    for m in game_map:
        print(''.join(m))

# 강사님 코드
dr = (-1,1,0,0)
dc = (0,0,-1,1)
dir_map = {'U':0,'D':1,'L':2,'R':3}

def solve():
    for c in commands:
        if c == 'S': shoot()
        else: move(dir_map[c])

    temp = {0:'^',1:'v',2:'<',3:'>'}
    game_map[tank_dir][tank_c] = temp[tank_dir]

    print(f'#{tc}', end='')
    for line in game_map: print(''.join(line))

def shoot():
    nr, nc = tank_r, tank_c
    while True:
        nr += dr[tank_dir]
        nc += dc[tank_dir]
        if nr < 0 or nr >= H or nc < 0 or nc >= W or game_map[nr][nc] == '#': break
        elif game_map[nr][nc] == '*':
            game_map[nr][nc] = '.'
            break

def move(dir):
    global tank_dir, tank_r, tank_c
    tank_dir = dir
    nr = tank_r + dr[tank_dir]
    nc = tank_c + dc[tank_dir]
    if 0 <= nr < H and 0 <= nc < W and game_map[nr][nc] == '.':
        tank_r, tank_c = nr, nc

TC = int(input())
for tc in range(1,TC+1):
    shape_map = {'^':0,'v':1,'<':2,'>':3}
    H,W = map(int, input().split())
    game_map = [list(input()) for _ in range(H)]

    tank_r, tank_c = -1, -1
    for r in range(H):
        for c in range(W):
            if game_map[r][c] in ('<','>','v','^'):
                tank_r, tank_c = r, c
                tank_dir = shape_map[game_map[r][c]]
                game_map[r][c] = '.'
                break
        if tank_r != -1: break

    cnt_command = int(input())
    commands = input()

    solve()