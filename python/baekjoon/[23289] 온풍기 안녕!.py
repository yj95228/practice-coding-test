'''
- 벽을 고려하지 않고 온풍기 바람 구현하는 것조차 2시간 걸림
- 벽 때문에 바람이 지나갈 수 없게 막는 것을 문제를 제대로 안 읽어서 잘못 구현했다가 뒤늦게 바꿈
- 13:55부터 밥먹는 시간 포함 18:36 제출이니까 대략 4시간 반 걸림...
- 제출 성공: 126160kb 912ms
- 어떻게 더 빨리 풀 수 있을지 감이 안 오는데 4가지 방향별로 벽을 죄다 종이에 적어놓는게 그나마 최선일 것 같다 ㅠㅠ
- 다른 사람들 코드를 보니 아래와 같이 변경할 수 있을듯
    - 벽을 dict()로 구현
    - bfs가 아닌 for문으로 구현
'''
# https://www.acmicpc.net/problem/23288
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

R, C, K = map(int, input().split())
ipt = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
onpungs, check, garo, sero = [], [], [], []
dt = ((0,1),(0,-1),(-1,0),(1,0))
onpung = (
    ((0,1),(-1,1),(1,1)),
    ((0,-1),(-1,-1),(1,-1)),
    ((-1,0),(-1,-1),(-1,1)),
    ((1,0),(1,-1),(1,1)),
)
for _ in range(W):
    X, Y, T = map(int, input().split())
    if T == 0:
        garo.append((X-1,Y-1))
    else:
        sero.append((X-1,Y-1))

for r in range(R):
    for c in range(C):
        if ipt[r][c] == 5:
            check.append((r,c))
        elif ipt[r][c]:
            onpungs.append((r,c,ipt[r][c]-1))

def bfs(r,c,d):
    visited = [[False]*C for _ in range(R)]
    if d == 0:
        dx, dy = dt[d]
        sx, sy = r+dx, c+dy
        matrix[sx][sy] += 5
        visited[sx][sy] = True
        queue = deque([(sx, sy, 0)])
        while queue:
            r, c, num = queue.popleft()
            for dx, dy in onpung[d]:
                nx, ny = r+dx, c+dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and abs(nx-sx) <= ny-sy:
                    if (dx,dy) == (0,1) and (r,c) in sero: continue
                    elif (dx,dy) == (-1,1) and ((r,c) in garo or (r-1,c) in sero): continue
                    elif (dx,dy) == (1,1) and ((r+1,c) in garo or (r+1,c) in sero): continue
                    visited[nx][ny] = True
                    matrix[nx][ny] += 5-(ny-sy)
                    if 5-(ny-sy): queue.append((nx,ny,num+1))
    elif d == 1:
        dx, dy = dt[d]
        sx, sy = r+dx, c+dy
        matrix[sx][sy] += 5
        visited[sx][sy] = True
        queue = deque([(sx, sy, 0)])
        while queue:
            r, c, num = queue.popleft()
            for dx, dy in onpung[d]:
                nx, ny = r+dx, c+dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and abs(nx-sx) <= sy-ny:
                    if (dx,dy) == (0,-1) and (nx,ny) in sero: continue
                    elif (dx,dy) == (-1,-1) and ((r,c) in garo or (nx,ny) in sero): continue
                    elif (dx,dy) == (1,-1) and ((r+1,c) in garo or (nx,ny) in sero): continue
                    visited[nx][ny] = True
                    matrix[nx][ny] += 5-(sy-ny)
                    if 5-(sy-ny): queue.append((nx,ny,num+1))
    elif d == 2:
        dx, dy = dt[d]
        sx, sy = r+dx, c+dy
        matrix[sx][sy] += 5
        visited[sx][sy] = True
        queue = deque([(sx, sy, 0)])
        while queue:
            r, c, num = queue.popleft()
            for dx, dy in onpung[d]:
                nx, ny = r+dx, c+dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and abs(ny-sy) <= sx-nx:
                    if (dx,dy) == (-1,0) and (r,c) in garo: continue
                    elif (dx,dy) == (-1,-1) and ((r,c-1) in garo or (r,c-1) in sero): continue
                    elif (dx,dy) == (-1,1) and ((r,c+1) in garo or (r,c) in sero): continue
                    visited[nx][ny] = True
                    matrix[nx][ny] += 5-(sx-nx)
                    if 5-(sx-nx): queue.append((nx,ny,num+1))
    else:
        dx, dy = dt[d]
        sx, sy = r+dx, c+dy
        matrix[sx][sy] += 5
        visited[sx][sy] = True
        queue = deque([(sx, sy, 0)])
        while queue:
            r, c, num = queue.popleft()
            for dx, dy in onpung[d]:
                nx, ny = r+dx, c+dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and abs(ny-sy) <= nx-sx:
                    if (dx,dy) == (1,0) and (nx,ny) in garo: continue
                    elif (dx,dy) == (1,-1) and ((nx,ny) in garo or (r,c-1) in sero): continue
                    elif (dx,dy) == (1,1) and ((nx,ny) in garo or (r,c) in sero): continue
                    visited[nx][ny] = True
                    matrix[nx][ny] += 5-(nx-sx)
                    if 5-(nx-sx): queue.append((nx,ny,num+1))

matrix = [[0]*C for _ in range(R)]
for choco in range(1,102):
    if choco == 101:
        print(101)
        break

    # 온풍기 바람
    for r, c, d in onpungs:
        bfs(r, c, d)

    # 온도 조절
    new_matrix = [row[:] for row in matrix]
    for r in range(R):
        for c in range(C):
            if matrix[r][c]:
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < R and 0 <= ny < C and matrix[r][c] > matrix[nx][ny]:
                        if (dx, dy) == (1,0) and (nx,ny) in garo: continue
                        elif (dx, dy) == (-1,0) and (r,c) in garo: continue
                        elif (dx, dy) == (0,1) and (r,c) in sero: continue
                        elif (dx, dy) == (0,-1) and (nx,ny) in sero: continue
                        diff = (matrix[r][c]-matrix[nx][ny])//4
                        new_matrix[nx][ny] += diff
                        new_matrix[r][c] -= diff

    for r in range(1,R-1):
        if new_matrix[r][0] > 0: new_matrix[r][0] -= 1
        if new_matrix[r][C-1] > 0: new_matrix[r][C-1] -= 1
    for c in range(C):
        if new_matrix[0][c] > 0: new_matrix[0][c] -= 1
        if new_matrix[R-1][c] > 0: new_matrix[R-1][c] -= 1

    for r, c in check:
        if new_matrix[r][c] < K:
            break
    else:
        print(choco)
        break

    matrix = new_matrix