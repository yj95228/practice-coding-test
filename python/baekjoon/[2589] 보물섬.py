import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [['W']*(M+2)] + [['W'] + list(input().rstrip()) + ['W'] for _ in range(N)] + [['W']*(M+2)]
answer = 0
for r in range(1,N+1):
    for c in range(1,M+1):
        if matrix[r][c] == 'W': continue
        queue = deque([(r,c,0)])
        visited = [[False]*(M+2) for _ in range(N+2)]
        visited[r][c] = True
        mx = 0
        while queue:
            r, c, distance = queue.popleft()
            mx = max(distance, mx)
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not visited[nx][ny] and matrix[nx][ny] == 'L':
                    visited[nx][ny] = True
                    queue.append((nx,ny,distance+1))
        answer = max(mx, answer)
print(answer)