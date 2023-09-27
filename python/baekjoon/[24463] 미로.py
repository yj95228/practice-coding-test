# https://www.acmicpc.net/problem/24463
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
sr, sc, er, ec = None, None, None, None
new_matrix = [row[:] for row in matrix]
for r in range(N):
    for c in range(M):
        if matrix[r][c] == '.':
            new_matrix[r][c] = '@'
            if r == 0 or c == 0 or r == N-1 or c == M-1:
                if sr is None and sc is None:
                    sr, sc = r, c
                else:
                    er, ec = r, c

visited = [[[] for _ in range(M)] for _ in range(N)]
queue = deque([(sr,sc)])
visited[sr][sc] = 'end'
while queue:
    r, c = queue.popleft()
    if (r,c) == (er,ec):
        while True:
            before = visited[r][c]
            if before == 'end':
                new_matrix[er][ec] = '.'
                break
            x, y = before
            new_matrix[x][y] = '.'
            r, c = x, y
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] == '.':
            visited[nx][ny] = (r,c)
            queue.append((nx,ny))

for row in new_matrix:
    print(*row, sep='')