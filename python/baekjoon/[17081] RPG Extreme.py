import sys
input = sys.stdin.readline

def hurt(r, c):
    global hp, dead
    damage = 1 if acc[acc_name['DX']] else 5
    if hp <= damage:
        hp = 0
        return lose('SPIKE TRAP')
    else:
        hp -= damage
    move(r, c)

def get_item(r, c):
    t, s = item_info[(r, c)]
    A[r][c] = EMPTY
    if t == 'W':
        global weapon
        weapon = s
    elif t == 'A':
        global shield
        shield = s
    else:
        if sum(acc) >= 4: return
        idx = acc_name[s]
        if acc[idx]: return
        acc[idx] = 1

def level_up():
    global level, hp, max_hp, attack, defence, exp
    level += 1
    max_hp += 5
    hp = max_hp
    attack += 2
    defence += 2
    exp = 0

def win(r, c, e):
    global hp, exp
    if acc[acc_name['HR']]:
        hp = min(hp+3, max_hp)
    rate = 1.2 if acc[acc_name['EX']] else 1
    exp += (e*rate)//1
    if exp >= 5*level:
        level_up()
    A[r][c] = EMPTY
    move(r, c)

def lose(txt):
    global hp, relive, dead, message
    if acc[acc_name['RE']]:
        relive = True
        acc[acc_name['RE']] = 0
        hp = max_hp
        move(ssr, ssc)
    else:
        hp = 0
        dead = True
        message = f'YOU HAVE BEEN KILLED BY {txt}..'
        return True

def fight(r, c, boss=False):
    global hp
    s, w, a, h, e = monster_info[(r, c)]
    attack1, fence, rate = attack+weapon, defence+shield, 1

    if acc[acc_name['CO']]:
        rate *= 3 if acc[acc_name['DX']] else 2

    skill1 = max(1, attack1*rate-a)
    damage1 = max(1, w-fence)
    skill, damage = max(1, (attack+weapon)-a), damage1

    if boss and acc[acc_name['HU']]:
        hp, damage1 = max_hp, 0

    # 첫번째 공격
    h -= skill1
    if h <= 0:
        return win(r, c, e)
    hp -= damage1
    if hp <= 0:
        return lose(s)

    # 이후
    while True:
        h -= skill
        if h <= 0:
            return win(r, c, e)
        hp -= damage
        if hp <= 0:
            return lose(s)

def move(r, c):
    global sr, sc
    sr, sc = r, c

def complete():
    if not dead:
        A[sr][sc] = '@'
    for r in range(1, N+1):
        for c in range(1, M+1):
            print(A[r][c], end='')
        print()
    print(f'Passed Turns : {turn}')
    print(f'LV : {level}')
    print(f'HP : {hp}/{max_hp}')
    print(f'ATT : {attack}+{weapon}')
    print(f'DEF : {defence}+{shield}')
    print(f'EXP : {int(exp)}/{level*5}')
    print(message)

N, M = map(int, input().split())
A = [['#']*(M+2)] + [['#'] + list(input().rstrip()) + ['#'] for _ in range(N)] + [['#']*(M+2)]
comm = list(input().rstrip())
dt = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
level, hp, max_hp, attack, defence, exp, relive, dead = 1, 20, 20, 2, 2, 0, False, False
sr, sc, er, ec = None, None, None, None
ME, EMPTY, WALL, BOX, HURT, MONSTER, BOSS = '@', '.', '#', 'B', '^', '&', 'M'
monster, item = 0, 0
monster_info, item_info = dict(), dict()
weapon, shield, acc = 0, 0, [0]*7
acc_name = {x: idx for idx, x in enumerate(['HR', 'RE', 'CO', 'EX', 'DX', 'HU', 'CU'])}
for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r][c] == ME:
            sr, sc = r, c
            A[r][c] = EMPTY
        elif A[r][c] == BOX:
            item += 1
        elif A[r][c] == MONSTER:
            monster += 1
        elif A[r][c] == BOSS:
            monster += 1
for _ in range(monster):
    r, c, s, w, a, h, e = map(lambda x: int(x) if x.isdigit() else x, input().split())
    monster_info[(r, c)] = [s, w, a, h, e]
for _ in range(item):
    r, c, t, s = map(lambda x: int(x) if x.isdigit() else x, input().split())
    item_info[(r, c)] = [t, s]

ssr, ssc = sr, sc   # 첫 시작 위치 기억하기
message = ''
# EMPTY, WALL, BOX, HURT, MONSTER, BOSS
for turn, d in enumerate(comm, start=1):
    dx, dy = dt[d]
    nx, ny = sr+dx, sc+dy
    if A[nx][ny] == EMPTY:
        move(nx, ny)
    elif A[nx][ny] == WALL:
        if A[sr][sc] == HURT:
            if hurt(sr, sc): break
    elif A[nx][ny] == BOX:
        get_item(nx, ny)
        A[nx][ny] = EMPTY
        move(nx, ny)
    elif A[nx][ny] == HURT:
        if hurt(nx, ny): break
    elif A[nx][ny] == MONSTER:
        if fight(nx, ny): break
    elif A[nx][ny] == BOSS:
        if fight(nx, ny, True):
            if relive:
                relive = False
                continue
        else:
            if relive:
                relive = False
                continue
            message = 'YOU WIN!'
        break
else: message = 'Press any key to continue.'
complete()