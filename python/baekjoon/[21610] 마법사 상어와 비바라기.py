# https://www.acmicpc.net/problem/21610
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# [1] 비구름 생성
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
for _ in range(M):
    D, S = map(int, input().split())
    dt = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

    # [2] 이동
    cloud = list(map(lambda x: [(x[0]+S*dt[D-1][0])%N, (x[1]+S*dt[D-1][1])%N], cloud))

    # [3] 비 내리기
    visited = [[False]*N for _ in range(N)]
    for r,c in cloud:
        matrix[r][c] += 1
        visited[r][c] = True

    # [4] 물 복사
    for r,c in cloud:
        rain = 0
        for dx, dy in ((1,1),(-1,-1),(1,-1),(-1,1)):
            if 0 <= r+dx < N and 0 <= c+dy < N and matrix[r+dx][c+dy]:
                rain += 1
        matrix[r][c] += rain

    # [5] 구름 만들기
    new_cloud = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] >= 2 and not visited[r][c]:
                matrix[r][c] -= 2
                new_cloud.append([r,c])
    cloud = new_cloud

print(sum(sum(matrix,[])))

# 2차 풀이
'''
- 1차. 13:43 ~ 14:08 c를 d로 오타내고 dt (1,0)를 (0,1)로 오타냄.. (117016kb, 496ms)
- 2차. 과거의 내가 속도가 더 빨라서 보니까 in은 오래 걸려서 룩업테이블로 바꾸기 (116244kb, 184ms)
'''
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dt = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for _ in range(M):
    d, s = map(int, input().split())
    dx, dy = dt[d-1]
    visited = [[False]*N for _ in range(N)]
    magic = []
    for r, c in cloud:
        nx, ny = (r+s*dx)%N, (c+s*dy)%N
        matrix[nx][ny] += 1
        magic.append((nx,ny))
        visited[nx][ny] = True

    narr = [row[:] for row in matrix]
    for r, c in magic:
        water = 0
        for dx, dy in ((1,1),(1,-1),(-1,1),(-1,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny]:
                water += 1
        narr[r][c] += water

    cloud = []
    for r in range(N):
        for c in range(N):
            if narr[r][c] >= 2 and not visited[r][c]:
                narr[r][c] -= 2
                cloud.append((r,c))
    matrix = narr

print(sum(map(sum,matrix)))