# https://www.acmicpc.net/problem/1600
from sys import stdin
from collections import deque
from heapq import heappop, heappush
stdin = open('input.txt','r')
input = stdin.readline

K = int(input())
W, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dt = ((1,0),(0,1),(-1,0),(0,-1),(2,1),(1,2),(-2,-1),(-1,-2),(2,-1),(1,-2),(-2,1),(-1,2))
visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]
queue = deque([(0,0,0)])
visited[0][0][0] = 1
while queue:
    horse, r, c = queue.popleft()
    if (r,c) == (H-1, W-1):
        print(visited[horse][r][c]-1)
        break
    for d in range(12):
        if horse >= K and d >= 4: continue
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if 0 <= nx < H and 0 <= ny < W and not A[nx][ny]:
            if d < 4 and not visited[horse][nx][ny]:
                visited[horse][nx][ny] = visited[horse][r][c] + 1
                queue.append((horse, nx, ny))
            elif d >= 4 and not visited[horse+1][nx][ny]:
                visited[horse+1][nx][ny] = visited[horse][r][c] + 1
                queue.append((horse+1, nx, ny))
else: print(-1)