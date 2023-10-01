# https://www.acmicpc.net/problem/14923
from sys import stdin
from collections import deque
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N, M = map(int, input().split())
sr, sc = map(lambda x: int(x)-1, input().split())
er, ec = map(lambda x: int(x)-1, input().split())
matrix = [list(input().split()) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
visited[0][sr][sc] = 1
queue = deque([(0,sr,sc)])
while queue:
    wall, r, c = queue.popleft()
    if (r,c) == (er,ec):
        print(visited[wall][r][c]-1)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[wall][nx][ny]:
            if wall == 0 and matrix[nx][ny] == '1':
                visited[1][nx][ny] = visited[0][r][c] + 1
                queue.append((1,nx,ny))
            elif matrix[nx][ny] == '0':
                visited[wall][nx][ny] = visited[wall][r][c] + 1
                queue.append((wall,nx,ny))
else: print(-1)