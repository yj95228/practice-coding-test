# https://www.acmicpc.net/problem/10026
import sys

def dfs(r, c):
    visited[r][c] = True
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]\
        and matrix[r][c] == matrix[nx][ny]:
            dfs(nx, ny)

def d_dfs(r, c):
    d_visited[r][c] = True
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not d_visited[nx][ny]\
        and ((matrix[r][c] == matrix[nx][ny] == 'B')\
            or ((matrix[r][c] == 'R' or matrix[r][c] == 'G')\
                and (matrix[nx][ny] == 'R' or matrix[nx][ny] == 'G'))):
            d_dfs(nx, ny)

sys.setrecursionlimit(10000)
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
d_visited = [[False]*N for _ in range(N)]
able, disable = 0, 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            able += 1
            dfs(r, c)
        if not d_visited[r][c]:
            disable += 1
            d_dfs(r, c)
print(able, disable)