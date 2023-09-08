# https://www.acmicpc.net/problem/1926
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [['0']*(M+2)] + [['0'] + input().split() + ['0'] for _ in range(N)] + [['0']*(M+2)]
visited = [[False]*(M+2) for _ in range(N+2)]
cnt, answer = 0, 0
for r in range(1,N+1):
    for c in range(1,M+1):
        if not visited[r][c] and matrix[r][c] == '1':
            cnt += 1
            tmp = 0
            visited[r][c] = True
            queue = deque([(r,c)])
            while queue:
                x, y = queue.popleft()
                tmp += 1
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if not visited[nx][ny] and matrix[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append((nx,ny))
            answer = max(tmp, answer)
print(cnt,answer,sep='\n')