# https://www.acmicpc.net/problem/14442
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[K]*M for _ in range(N)]
queue = deque([(0,0,0,1)])
visited[0][0] = 0
while queue:
    wall, r, c, cnt = queue.popleft()
    if (r,c) == (N-1, M-1):
        print(cnt)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and wall <= visited[nx][ny]:
            visited[nx][ny] -= 1
            if matrix[nx][ny] == '0':
                queue.append((wall, nx, ny, cnt+1))
            elif matrix[nx][ny] == '1':
                queue.append((wall+1, nx, ny, cnt+1))
else: print(-1)