# https://www.acmicpc.net/problem/2665
from sys import stdin
from heapq import heappop, heappush
stdin = open('input.txt')
input = stdin.readline

N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1
queue = [(0,0,0)]
while queue:
    wall, r, c = heappop(queue)
    if (r, c) == (N-1, N-1):
        print(wall)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            if matrix[nx][ny] == '1':
                heappush(queue, (wall, nx, ny))
            else:
                heappush(queue, (wall+1, nx, ny))