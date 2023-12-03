
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if not N: break
    A = [list(input().rstrip()) for _ in range(N)]
    sr, sc, er, ec = -1, -1, -1, -1
    sinhodng = 0
    for r in range(N):
        for c in range(M):
            if A[r][c] == 'A':
                sr, sc = r, c
                A[r][c] = '#'
            elif A[r][c] == 'B':
                er, ec = r, c
                A[r][c] = '#'
            elif A[r][c].isdigit():
                sinhodng += 1
    sinho = [[] for _ in range(sinhodng)]
    for _ in range(sinhodng):
        idx, sh, a, b, = input().split()
        sinho[int(idx)] = [sh, int(a), int(b)]
    V = [[987654321]*M for _ in range(N)]
    V[sr][sc] = 0
    queue = [(0, sr, sc)]
    while queue:
        time, r, c = heappop(queue)
        if (r, c) == (er, ec): print(time); break
        for d, (dx, dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M:
                if A[nx][ny] == '.': continue
                elif A[nx][ny] == '#':
                    if time+1 < V[nx][ny]:
                        V[nx][ny] = time+1
                        heappush(queue, (time+1, nx, ny))
                    continue
                sh, a, b = sinho[int(A[nx][ny])]
                if sh == '-':
                    if d%2: #동서
                        ntime = time+1 if time%(a+b) < a else time//(a+b)*(a+b)+a+b+1
                    else:   #남북
                        ntime = time+1 if time%(a+b) >= a else time//(a+b)*(a+b)+a+1
                else:
                    if d%2: #동서
                        ntime = time+1 if time%(a+b) >= b else time//(a+b)*(a+b)+b+1
                    else:   #남북
                        ntime = time+1 if time%(a+b) < b else time//(a+b)*(a+b)+a+b+1
                if ntime < V[nx][ny]:
                    V[nx][ny] = ntime
                    heappush(queue, (ntime, nx, ny))
    else: print('impossible')
    input()