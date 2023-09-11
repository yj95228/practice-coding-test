# 1차 제출: 재귀로 풀었더니 런타임 에러 (RecursionError)
# 2차 제출: for문으로 수정 (124492kb, 304ms)
# https://www.acmicpc.net/problem/1913
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
matrix = [[0]*N for _ in range(N)]
dt = ((0,-1),(-1,0),(0,1),(1,0))
r, c, d = N//2, N//2, 0
matrix[r][c] = 1
for num in range(2,N*N+1):
    dx, dy = dt[(d+1)%4]
    nx, ny = r+dx, c+dy
    if not matrix[nx][ny]:
        matrix[nx][ny] = num
        d = (d+1)%4
    else:
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        matrix[nx][ny] = num
    r, c = nx, ny

for row in matrix:
    print(*row)

M = int(input())
for r in range(N):
    for c in range(N):
        if matrix[r][c] == M:
            print(r+1, c+1)