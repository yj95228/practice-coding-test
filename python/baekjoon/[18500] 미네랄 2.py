import sys
input = sys.stdin.readline

def down():
    G = [[0]*M for _ in range(N)]
    g = 1
    for r in range(N-1, -1, -1):
        for c in range(M):
            if G[r][c] or A[r][c] == '.': continue
            G[r][c] = g
            stack = [(r, c)]
            group = [(r, c)]
            while stack:
                xx, yy = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = xx+dx, yy+dy
                    if 0 <= nx < N and 0 <= ny < M and not G[nx][ny] and A[nx][ny] == 'x':
                        G[nx][ny] = g
                        stack.append((nx, ny))
                        group.append((nx, ny))
            g += 1
            mn = N
            for x, y in group:
                rr = 0
                flag = False
                while True:
                    rr += 1
                    if x+rr == N:
                        flag = True
                        break
                    elif G[x+rr][y] == G[x][y]: break
                    elif A[x+rr][y] == 'x':
                        flag = True
                        break
                if flag:
                    mn = min(mn, rr-1)
            if mn:
                for r, c in sorted(group, key=lambda x: (x[1], -x[0])):
                    A[r + mn][c], A[r][c] = A[r][c], A[r + mn][c]
                    G[r + mn][c], G[r][c] = G[r][c], G[r + mn][c]

def throw(x, left):
    if left:
        for c in range(M):
            if A[N-x][c] == 'x':
                A[N-x][c] = '.'
                down()
                return
    else:
        for c in range(M-1, -1, -1):
            if A[N-x][c] == 'x':
                A[N-x][c] = '.'
                down()
                return

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
K = int(input())
arr = list(map(int, input().split()))
left = True
for x in arr:
    throw(x, left)
    left ^= 1

for row in A:
    print(''.join(row))