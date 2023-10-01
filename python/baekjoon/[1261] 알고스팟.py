# https://www.acmicpc.net/problem/1261
import sys
from heapq import heappop, heappush
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = [(1,0,0)]
visited[0][0] = 1

while queue:
    wall, r, c = heappop(queue)
    
    if (N-1,M-1) == (r,c):
        print(wall-1)
        break
        
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and (not visited[nx][ny] or wall < visited[nx][ny]):
            visited[nx][ny] = wall
            if matrix[nx][ny] == '0':
                heappush(queue, (wall, nx, ny))
            else:
                heappush(queue, (wall+1, nx, ny))