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