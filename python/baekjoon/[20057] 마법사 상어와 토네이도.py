# 1차 제출: (70분 소요) 121508kb, 384ms
# https://www.acmicpc.net/problem/20057
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def blow(r,c,d):
    global answer
    dx, dy = dt[d]
    nr, nc = r+dx, c+dy
    total = matrix[nr][nc] + matrix[r][c]

    # 바람 불기
    if d%2 == 0:
        for rate, dx, dy in ((10,-1,-2),(10,1,-2),(7,-1,-1),(7,1,-1),(2,-2,-1),(2,2,-1),(1,-1,0),(1,1,0),(5,0,-3)):
            sand = matrix[nr][nc]*rate//100
            total -= sand
            if d == 2: dy *= -1
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N:
                matrix[nx][ny] += sand
            else:
                answer += sand
    else:
        for rate, dx, dy in ((10,2,-1),(10,2,1),(7,1,-1),(7,1,1),(2,1,-2),(2,1,2),(1,0,-1),(1,0,1),(5,3,0)):
            sand = matrix[nr][nc]*rate//100
            total -= sand
            if d == 3: dx *= -1
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N:
                matrix[nx][ny] += sand
            else:
                answer += sand
    # α
    dr, dc = nr+dt[d][0], nc+dt[d][1]
    if 0 <= dr < N and 0 <= dc < N:
        matrix[nr+dt[d][0]][nc+dt[d][1]] += total
    else:
        answer += total
    # y, x
    matrix[nr][nc], matrix[r][c] = 0, 0
    return nr, nc

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
r, c, d, s = N//2, N//2, 0, 0
dt = ((0,-1),(1,0),(0,1),(-1,0))
answer = 0
for i in range(1,N*N+1):
    visited[r][c] = True
    r, c = blow(r,c,d)
    if not visited[r+dt[(d+1)%4][0]][c+dt[(d+1)%4][1]]:
        d = (d+1)%4
print(answer)

# 2차 풀이
'''
- 1차. 09:45 ~ 10:47
- 달팽이 배열 만드는거 오래 걸림
- 모래가 밖으로 날릴 때 total에서 안 빼줌
'''
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
visited[N//2][N//2] = True
snail = [(N//2,N//2)]
dt = ((0,-1),(1,0),(0,1),(-1,0))
d = -1
for _ in range(N*N-1):
    r, c = snail[-1]
    dx, dy = dt[(d+1)%4]
    nx, ny = r+dx, c+dy
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        snail.append((nx,ny))
        d = (d+1)%4
    else:
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        visited[nx][ny] = True
        snail.append((nx,ny))
snail.append((0,-1))
rates = [
    [(1,-1,0),(1,1,0),(7,-1,-1),(7,1,-1),(2,-2,-1),(2,2,-1),(10,-1,-2),(10,1,-2),(5,0,-3)],
    [(1,0,-1),(1,0,1),(7,1,-1),(7,1,1),(2,1,-2),(2,1,2),(10,2,-1),(10,2,1),(5,3,0)],
    [(1,-1,0),(1,1,0),(7,-1,1),(7,1,1),(2,-2,1),(2,2,1),(10,-1,2),(10,1,2),(5,0,3)],
    [(1,0,-1),(1,0,1),(7,-1,-1),(7,-1,1),(2,-1,-2),(2,-1,2),(10,-2,-1),(10,-2,1),(5,-3,0)],
]
answer = 0
for i, (r, c) in enumerate(snail[:-1]):
    x1, y1 = snail[i+1]
    x2, y2 = snail[i]
    dx, dy = x1-x2, y1-y2
    nx, ny = r+dx, c+dy

    if 0 <= nx < N and 0 <= ny < N:
        total = matrix[nx][ny]
        d = 0
        for dd, (xx, yy) in enumerate(dt):
            if (xx,yy) == (dx,dy):
                d = dd
                break

        for rate, dx, dy in rates[d]:
            sand = rate*matrix[nx][ny]//100
            nr, nc = r+dx, c+dy
            if 0 <= nr < N and 0 <= nc < N:
                matrix[nr][nc] += sand
                total -= sand
            else:
                total -= sand
                answer += sand

        dx, dy = x1-x2, y1-y2
        nr, nc = nx+dx, ny+dy
        if 0 <= nr < N and 0 <= nc < N:
            matrix[nr][nc] += total
        else:
            answer += total
        matrix[nx][ny] = 0

    else:
        answer += matrix[r][c]
        matrix[r][c] = 0

print(answer)