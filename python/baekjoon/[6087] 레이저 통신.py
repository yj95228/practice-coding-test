# https://www.acmicpc.net/problem/6087
from sys import stdin
from heapq import heappop, heappush
stdin = open('input.txt','r')
input = stdin.readline

W, H = map(int, input().split())
A = [['*']*(W+2)] + [['*'] + list(input().rstrip()) + ['*'] for _ in range(H)] + [['*']*(W+2)]
V = [[[987654321]*(W+2) for _ in range(H+2)] for _ in range(4)]
dt = ((1,0),(0,1),(-1,0),(0,-1))
sr, sc, er, ec = None, None, None, None
for r in range(1, H+1):
    for c in range(1, W+1):
        if A[r][c] == 'C':
            if er is None:
                A[r][c] = '.'
                er, ec = r, c
            else:
                for d in range(4):
                    V[d][r][c] = 0
                A[r][c] = '.'
                sr, sc = r, c

queue = [(-1, sr, sc, -1)]
while queue:
    turn, r, c, d = heappop(queue)
    if (r, c) == (er, ec):
        print(turn)
        break
    for t in range(4):
        dx, dy = dt[t]
        nx, ny = r+dx, c+dy
        if A[nx][ny] == '*': continue
        if d == t:
            # 같은 방향
            if turn < V[t][nx][ny]:
                V[t][nx][ny] = turn
                heappush(queue, (turn, nx, ny, t))
        else:
            # 다른 방향
            if turn+1 < V[t][nx][ny]:
                V[t][nx][ny] = turn+1
                heappush(queue, (turn+1, nx, ny, t))