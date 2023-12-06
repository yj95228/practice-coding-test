import sys
input = sys.stdin.readline

def solve():
    global sr, sc
    for now, t in enumerate(arr, start=1):
        dx, dy = dt[t]
        nx, ny = sr + dx, sc + dy
        if 0 <= nx < N and 0 <= ny < N and not A[nx][ny]:
            sr, sc = nx, ny

        for i, (r, c, kind, d, s) in enumerate(zombie):
            dx, dy = dt[d]
            if kind == 0:
                for k in range(1, s + 1):
                    nx, ny = r + k * dx, c + k * dy
                    if 0 <= nx < N and 0 <= ny < N and not A[nx][ny]:
                        zombie[i][0], zombie[i][1] = nx, ny
                    else:
                        zombie[i][3] = rotate[d]
                        break
                rr, cc = zombie[i][0], zombie[i][1]

            else:
                for k in range(1, s + 1):
                    nx, ny = r + k * dx, c + k * dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not A[nx][ny]:  # 벽이 아니면
                            zombie[i][0], zombie[i][1] = nx, ny
                        else:  # 벽이면
                            A[nx][ny] = 0
                            break
                    else: break

                rr, cc = zombie[i][0], zombie[i][1]

                mx, md = -1, None
                for dd, dx, dy in (('U', -1, 0), ('R', 0, 1), ('D', 1, 0), ('L', 0, -1)):
                    go, cnt = 1, 0
                    while True:
                        nx, ny = rr + go * dx, cc + go * dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if A[nx][ny]: cnt += 1
                        else:
                            if mx < cnt: mx, md = cnt, dd
                            break
                        go += 1
                zombie[i][3] = md
        for r, c, _, _, _ in zombie:
            if (r, c) == (sr, sc): return now, 'DEAD...'
        if day == now: return ['ALIVE!']

N = int(input())
A = [[0]*N for _ in range(N)]
arr = list(input().rstrip()) + ['S']
sr, sc = map(lambda x: int(x)-1, input().split())
W = int(input())
for _ in range(W):
    r, c = map(lambda x: int(x)-1, input().split())
    A[r][c] = 1
Z = int(input())
zombie = []
dt = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1),'S':(0,0)}
rotate = {'U':'D', 'D':'U', 'L':'R', 'R':'L'}
for _ in range(Z):
    r, c, kind, d, s = input().split()
    zombie.append([int(r)-1, int(c)-1, int(kind), d, int(s)])
day = int(input())
print(*solve(), sep='\n')