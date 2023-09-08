# https://www.acmicpc.net/problem/21736
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
visited = [[False]*M for _ in range(N)]
answer, x, y = 0, 0, 0
for r in range(N):
    arr = list(input().rstrip())
    if 'I' in arr:
        x, y = r, arr.index('I')
    matrix.append(arr)

queue = deque([(x,y)])
visited[x][y] = True
while queue:
    r, c = queue.popleft()
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and\
        not visited[nx][ny] and matrix[nx][ny] != 'X':
            visited[nx][ny] = True
            if matrix[nx][ny] == 'P': answer += 1
            queue.append((nx,ny))
print(answer or 'TT')