# https://www.acmicpc.net/problem/30036
I, N, K = map(int, input().split())
inks = list(input().rstrip())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc = None, None
for r in range(N):
    for c in range(N):
        if A[r][c] == '@':
            sr, sc = r, c
            A[r][c] = '.'
i, ink = 0, 0
dt = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
lst = list(input().rstrip())
for k in lst:
    if k == 'j':
        ink += 1
    elif k == 'J':
        for r in range(sr-ink, sr+ink+1):
            for c in range(sc-ink, sc+ink+1):
                if abs(r-sr)+abs(c-sc) <= ink and 0 <= r < N and 0 <= c < N and A[r][c] != '.':
                    A[r][c] = inks[i]
        ink = 0
        i = (i+1)%len(inks)
    else:
        dx, dy = dt[k]
        nx, ny = sr+dx, sc+dy
        if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == '.':
            sr, sc = nx, ny
A[sr][sc] = '@'
for row in A:
    print(''.join(row))