import sys
input = sys.stdin.readline

def move(x):
    global answer, sr, sc, OVERDOSE, drug
    dx, dy = dt[x]
    nx, ny = sr+speed*dx, sc+speed*dy
    if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
        answer += 1
        sr, sc = nx, ny
        if OVERDOSE:
            OVERDOSE -= 1
            if not OVERDOSE: drug = 0

def attack(x):
    global answer, sr, sc, exp, saguri, power, level, require
    answer += 3
    dx, dy = dt[x]
    for i in range(1, saguri+1):
        nx, ny = sr+i*dx, sc+i*dy
        if A[nx][ny] == '*': break
        elif A[nx][ny] == 'm':
            idx = monster.get((nx, ny))
            h, d, e = mh[idx], md[idx], mexp[idx]
            if power >= d:
                skill = power-d
                h -= skill
                if h <= 0:
                    A[nx][ny] = '.'
                    exp += e
                    mh[idx] = 0
                else:
                    mh[idx] = h
    while exp >= require:
        power += level
        level += 1
        exp -= require
        saguri += 1
        require += 10

def eat(x):
    global speed, answer, drug, OVERDOSE
    if x == 'u':
        speed += 1
    elif x == 'd':
        speed = max(0, speed-1)
    answer += 2
    drug += 1
    if drug == 5: OVERDOSE = 10

def pprint(A):
    print(level, exp)
    print(answer)
    A = [row[:] for row in A]
    A[er][ec] = 'g'
    A[sr][sc] = 'p'
    for row in A:
        print(''.join(row))
    print(*[h for h in mh if h > 0])

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
K = int(input())
mh = list(map(int, input().split()))
md = list(map(int, input().split()))
mexp = list(map(int, input().split()))
S = int(input())
arr = input().split()
power, saguri, speed, require, exp, level = 5, 1, 1, 10, 0, 1
dt = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
sr, sc, er, ec = None, None, None, None
monster = dict()
m = 0
for r in range(N):
    for c in range(M):
        if A[r][c] == 'p':
            sr, sc = r, c
            A[r][c] = '.'
        elif A[r][c] == 'g':
            er, ec = r, c
            A[r][c] = '.'
        elif A[r][c] == 'm':
            monster[(r, c)] = m
            m += 1
answer, drug, OVERDOSE = 0, 0, 0
for x in arr:
    if x in ('u','d','l','r'):
        move(x)
    elif x == 'w':
        answer += 1
        if OVERDOSE:
            OVERDOSE -= 1
            if not OVERDOSE: drug = 0
    elif not OVERDOSE and x in ('au','ad','al','ar'):
        attack(x[1])
    elif not OVERDOSE and x in ('du','dd'):
        eat(x[1])
    elif not OVERDOSE and x == 'c':
        if (sr, sc) == (er, ec):
            break
pprint(A)