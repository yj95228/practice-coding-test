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