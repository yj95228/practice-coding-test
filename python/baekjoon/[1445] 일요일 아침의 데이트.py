# 1차 제출: 재귀로 dfs 풀었음 (시간 초과)
# 2차 제출: 쓰레기와 쓰레기 옆이 (0,0)이라면 가지치기 (시간 초과)
# 3차 제출: heapq로 풀었음 (116516kb, 200ms)
# https://www.acmicpc.net/problem/1022
import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
garbage, near, sr, sc, er, ec = N*M, N*M, 0, 0, 0, 0
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'g':
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '.':
                    matrix[nx][ny] = 'N'
        elif matrix[r][c] == 'S':
            sr, sc = r, c
        elif matrix[r][c] == 'F':
            er, ec = r, c
queue = []
heappush(queue, (0,0,sr,sc))
visited = [[False]*M for _ in range(N)]
visited[sr][sc] = True
while queue:
    g, n, r, c = heappop(queue)
    if (r,c) == (er,ec):
        if g < garbage:
            garbage, near = g, n
        elif g == garbage:
            if n < near:
               near = n
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            if matrix[nx][ny] == '.' or matrix[nx][ny] == 'F':
                heappush(queue, (g,n,nx,ny))
            elif matrix[nx][ny] == 'N':
                heappush(queue, (g,n+1,nx,ny))
            elif matrix[nx][ny] == 'g':
                heappush(queue, (g+1,n,nx,ny))
print(garbage, near)