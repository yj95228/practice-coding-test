from sys import stdin
from collections import deque
stdin = open('input.txt')
input = stdin.readline

N, M, K = map(int, input().split())
matrix = [[0]*(M+2) for _ in range(N+2)]
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r][c] = 1
visited = [[0]*(M+2) for _ in range(N+2)]
answer = 0
for r in range(1,N+1):
    for c in range(1,M+1):
        if matrix[r][c] and not visited[r][c]:
            stack = [(r,c)]
            visited[r][c] = 1
            cnt = 1
            while stack:
                r, c = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if not visited[nx][ny] and matrix[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx, ny))
                        cnt += 1
            answer = max(cnt, answer)
print(answer)