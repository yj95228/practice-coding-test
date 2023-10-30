# https://www.acmicpc.net/problem/20926
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

TERRA, ROCK, HOLE, EXIT = 'T', 'R', 'H', 'E'
M, N = map(int, input().split())
A = [['H']*(M+2)] + [['H'] + list(input().rstrip()) + ['H'] for _ in range(N)] + [['H']*(M+2)]
D = [[987654321]*(M+2) for _ in range(N+2)]
sr, sc = None, None
for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r][c] == TERRA:
            A[r][c] = '0'
            sr, sc = r, c
            D[r][c] = 0

queue = [(0, sr, sc)]
while queue:
    time, r, c = heappop(queue)
    if A[r][c] == EXIT:
        print(time)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        s = 1
        sm = 0
        while True:
            nx, ny = r+s*dx, c+s*dy
            if A[nx][ny] != HOLE:
                if A[nx][ny] == EXIT:
                    if time+sm < D[nx][ny]:
                        D[nx][ny] = time+sm
                        heappush(queue, (time+sm, nx, ny))
                        break
                elif A[nx][ny] == ROCK:
                    nx, ny = nx-dx, ny-dy
                    if (r, c) != (nx, ny):
                        if time+sm < D[nx][ny]:
                            D[nx][ny] = time+sm
                            heappush(queue, (time+sm, nx, ny))
                        break
                    else: break
                else:
                    sm += int(A[nx][ny])
                s += 1
            else: break
else: print(-1)