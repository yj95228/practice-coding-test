import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
game_map = [['B']*(M+2)] + [['B'] + list(input().rstrip()) + ['B'] for _ in range(N)] + [['B']*(M+2)]
rotate = {'A':'A', 'B':'B', 'C':'D', 'D':'C'}
V = [[set() for _ in range(M+2)] for _ in range(N+2)]
V[1][1].add(''.join(map(lambda x: ''.join(x), game_map)))
queue = deque([(0, 1, 1, [row[:] for row in game_map])])
while queue:
    turn, r, c, G = queue.popleft()
    if (r, c) == (N, M):
        print(turn)
        break
    g = ''.join(map(lambda x: ''.join(x), G))
    for d, (dx, dy) in enumerate(((1,0),(-1,0),(0,1),(0,-1))):
        nx, ny = r+dx, c+dy
        if g not in V[nx][ny]:
            if d < 2 and G[r][c] in ('A','C') and G[nx][ny] in ('A','C'):
                V[nx][ny].add(g)
                queue.append((turn+1, nx, ny, [row[:] for row in G]))
            elif d >= 2 and G[r][c] in ('A','D') and G[nx][ny] in ('A','D'):
                V[nx][ny].add(g)
                queue.append((turn+1, nx, ny, [row[:] for row in G]))
    for rr in range(1, N+1):
        G[rr][c] = rotate.get(G[rr][c])
    for cc in range(1, M+1):
        G[r][cc] = rotate.get(G[r][cc])
    new_map = ''.join(map(lambda x: ''.join(x), G))
    if new_map not in V[r][c]:
        V[r][c].add(new_map)
        queue.append((turn+1, r, c, [row[:] for row in G]))
else: print(-1)