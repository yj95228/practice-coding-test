import sys
from collections import deque
input = sys.stdin.readline

def solve():
    turn = 0
    while queue:
        for _ in range(len(queue)):
            e, dd, r, c = queue.popleft()
            if e == 1 and (r, c) == (er2, ec2):
                return turn
            elif e == 2 and (r, c) == (er1, ec1):
                return turn
            for d, (dx, dy) in enumerate(dt):
                if d == dd: continue
                nx, ny = r + dx, c + dy
                if A[nx][ny] != '#':
                    ne = e
                    if not e:
                        if (nx, ny) == (er1, ec1):
                            ne = 1
                        elif (nx, ny) == (er2, ec2):
                            ne = 2
                    if V[ne * 4 + d][nx][ny]: continue
                    V[ne * 4 + d][nx][ny] = turn + 1
                    queue.append((ne, d, nx, ny))
        turn += 1
    return -1

N, M = map(int, input().split())
A = [['#']*(M+2)] + [['#'] + list(input().rstrip()) + ['#'] for _ in range(N)] + [['#']*(M+2)]
dt = ((1,0),(0,1),(-1,0),(0,-1))
V = [[[0]*(M+2) for _ in range(N+2)] for _ in range(12)]
sr, sc, er1, ec1, er2, ec2 = None, None, None, None, None, None
queue = deque()
for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r][c] == 'S':
            sr, sc = r, c
            queue.append((0, -1, sr, sc))
        elif A[r][c] == 'C':
            if er1 is None:
                er1, ec1 = r, c
            else:
                er2, ec2 = r, c
print(solve())