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