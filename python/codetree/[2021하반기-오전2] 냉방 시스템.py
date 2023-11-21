'''
- 원래 있던 1,2,3,4,5도 에어컨 온도로 체크해줌
- 에어컨 방향 실수 너무 많이 함
- 온도 조절할 때 (1,0),(0,1) 순서 바꿔씀
'''
# https://www.codetree.ai/training-field/frequent-problems/problems/cooling-system/submissions?page=1&pageSize=20
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(r, c, d):
    visited = [[False]*N for _ in range(N)]
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    visited[nx][ny] = True
    heater[nx][ny] += 5            # 에어컨 바로 앞이 격자를 벗어나는 경우는 주어지지 않음
    strong = [0]*N
    if d == 0 or d == 2:
        for i in range(1,5):
            if 0 <= ny+i*dy < N:
                strong[ny+i*dy] = 5-i
        queue = deque([(nx, ny)])
        while queue:
            r, c = queue.popleft()
            for i, (dx, dy) in enumerate(bfs_dt[d]):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    for dd, ddx, ddy in bfs_wall[d][i]:
                        if (nx+ddx, ny+ddy) in wall[dd]: break
                    else:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        heater[nx][ny] += strong[ny]
    else:
        for i in range(1,5):
            if 0 <= nx+i*dx < N:
                strong[nx+i*dx] = 5-i
        queue = deque([(nx, ny)])
        while queue:
            r, c = queue.popleft()
            for i, (dx, dy) in enumerate(bfs_dt[d]):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    for dd, ddx, ddy in bfs_wall[d][i]:
                        if (nx+ddx, ny+ddy) in wall[dd]: break
                    else:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        heater[nx][ny] += strong[nx]

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dt = ((0,-1),(-1,0),(0,1),(1,0))

# 벽만들기
wall = [[] for _ in range(4)]
for _ in range(M):
    x, y, s = map(lambda x: int(x)-1, input().split())
    if s == -1:
        wall[0].append((x,y+1))
        wall[2].append((x,y))
    else:
        wall[1].append((x+1,y))
        wall[3].append((x,y))

# 체크할 곳과 에어컨 바람 만들어주기
bfs_dt = (
    ((0,-1),(-1,-1),(1,-1)),
    ((-1,0),(-1,-1),(-1,1)),
    ((0,1),(-1,1),(1,1)),
    ((1,0),(1,-1),(1,1))
)
bfs_wall = (
    ([(3,0,1)],[(3,0,1),(2,1,1)],[(3,0,1),(2,0,1)]),
    ([(2,1,0)],[(3,1,1),(2,1,0)],[(3,1,0),(2,1,0)]),
    ([(3,0,0)],[(3,0,0),(2,1,-1)],[(3,0,0),(2,0,-1)]),
    ([(2,0,0)],[(3,-1,1),(2,0,0)],[(3,-1,0),(2,0,0)]),
)
heater = [[0]*N for _ in range(N)]
check = []
for r in range(N):
    for c in range(N):
        if not matrix[r][c]: continue
        elif matrix[r][c] == 1:
            check.append((r,c))
            matrix[r][c] = 0
        else:
            # heater = [[0]*N for _ in range(N)]
            bfs(r, c, matrix[r][c]-2)
            matrix[r][c] = 0

for time in range(1,101):
    # 1. 에어컨 바람 나옴
    for r in range(N):
        for c in range(N):
            matrix[r][c] += heater[r][c]

    # 2. 시원한 공기 섞임
    narr = [row[:] for row in matrix]
    for r in range(N):
        for c in range(N):
            for i, (dx, dy) in enumerate(((1,0),(0,1))):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in wall[i+2]:
                    diff = abs(matrix[r][c]-matrix[nx][ny])//4
                    if not diff: continue
                    elif matrix[r][c] > matrix[nx][ny]:
                        narr[r][c] -= diff
                        narr[nx][ny] += diff
                    else:
                        narr[r][c] += diff
                        narr[nx][ny] -= diff

    # 3. 외벽 칸 시원함 1 감소
    for r in range(N):
        narr[r][0] = max(0, narr[r][0]-1)
        narr[r][N-1] = max(0, narr[r][N-1]-1)
    for c in range(1,N-1):
        narr[0][c] = max(0, narr[0][c]-1)
        narr[N-1][c] = max(0, narr[N-1][c]-1)

    # 4. 시원함 체크
    for r, c in check:
        if narr[r][c] < K:
            break
    else:
        print(time)
        break

    matrix = narr

else: print(-1)

# 2차 풀이
import sys
input = sys.stdin.readline

def aircon(x, y):
    d = A[x][y]-2
    dx, dy = dt[d]
    nx, ny = x+dx, y+dy
    V = [[0]*N for _ in range(N)]
    V[nx][ny] = 1
    queue = [(nx, ny)]
    B[nx][ny] += 5
    num = 4
    while queue and num:
        next_q = []
        for r, c in queue:
            for i, (dx, dy) in enumerate(wind[d]):
                for dd, ddx, ddy in air_walls[d][i]:
                    nnx, nny = r+ddx, c+ddy
                    if (nnx, nny) in wall[dd]: break
                else:
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
                        V[nx][ny] = 1
                        B[nx][ny] += num
                        next_q.append((nx, ny))
        queue = next_q
        num -= 1

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
wall = [[] for _ in range(4)]
for _ in range(M):
    x, y, s = map(int, input().split())
    if s == 0:  # 가로
        wall[1].append((x-2, y-1))
        wall[3].append((x-1, y-1))
    else:       # 세로
        wall[0].append((x-1, y-2))
        wall[2].append((x-1, y-1))
wind = [
    [(0,-1),(-1,-1),(1,-1)],
    [(-1,0),(-1,-1),(-1,1)],
    [(0,1),(-1,1),(1,1)],
    [(1,0),(1,-1),(1,1)]
]
air_walls = [
    [[(2,0,0)],[(2,-1,0),(1,-1,0)],[(2,1,0),(3,1,0)]],
    [[(3,0,0)],[(3,0,-1),(0,0,-1)],[(3,0,1),(2,0,1)]],
    [[(0,0,0)],[(0,-1,0),(1,-1,0)],[(0,1,0),(3,1,0)]],
    [[(1,0,0)],[(1,0,-1),(0,0,-1)],[(1,0,1),(2,0,1)]],
]
B = [[0]*N for _ in range(N)]
dt = ((0,-1),(-1,0),(0,1),(1,0))
check, side = [], []
for r in range(N):
    for c in range(N):
        if r in (0, N-1) or c in (0, N-1):
            side.append((r, c))
        if 2 <= A[r][c] <= 5:
            aircon(r, c)
        elif A[r][c] == 1:
            check.append((r, c))

C = [[0]*N for _ in range(N)]
for time in range(1, 100):
    # 1. 에어컨 바람 나오기
    for r in range(N):
        for c in range(N):
            C[r][c] += B[r][c]

    # 2. 시원한 공기 섞이기
    D = [row[:] for row in C]
    for r in range(N):
        for c in range(N):
            for d, (dx, dy) in enumerate(((1,0),(0,1))):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in wall[3-d]:
                    diff = abs(C[r][c]-C[nx][ny])//4
                    if not diff: continue
                    elif C[r][c] > C[nx][ny]:
                        D[r][c] -= diff
                        D[nx][ny] += diff
                    else:
                        D[r][c] += diff
                        D[nx][ny] -= diff

    # 3. 외벽 칸 시원함 1 감소
    for r, c in side:
        D[r][c] = max(D[r][c]-1, 0)

    # 4. 공기 체크
    for r, c in check:
        if D[r][c] < K: break
    else:
        print(time)
        break
    C = D
else: print(-1)