# https://www.acmicpc.net/problem/18405
from sys import stdin
from collections import deque
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
visited = [[0]*N for _ in range(N)]
viruses = [[] for _ in range(K)]
for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            viruses[matrix[r][c]-1].append((0, r, c, matrix[r][c]))
            visited[r][c] = 1
queue = deque(sum(viruses,[]))
while queue:
    time, r, c, virus = queue.popleft()
    if time > S:
        print(0)
        break
    elif (r,c) == (X-1, Y-1):
        print(virus)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = visited[r][c]+1
            matrix[nx][ny] = virus
            queue.append((time+1, nx, ny, virus))