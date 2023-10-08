# https://www.acmicpc.net/problem/2146
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(r, c, group):
    groups[r][c] = group
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not groups[nx][ny] and matrix[nx][ny] == '1':
                groups[nx][ny] = group
                queue.append((nx, ny))

def dari(r, c, group):
    global answer
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    queue = deque([(r, c, 0)])
    while queue:
        r, c, length = queue.popleft()
        if answer < length: return 987654321
        if groups[r][c] and groups[r][c] != group:
            return length-1
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and groups[nx][ny] != group:
                visited[nx][ny] = True
                queue.append((nx, ny, length+1))
    return 987654321

N = int(input())
matrix = [input().split() for _ in range(N)]

groups = [[0]*N for _ in range(N)]
group = 1
for r in range(N):
    for c in range(N):
        if matrix[r][c] == '0' or groups[r][c]: continue
        bfs(r, c, group)
        group += 1
        
answer = 987654321
for r in range(N):
    for c in range(N):
        if groups[r][c]:
            flag = False
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == '0':
                    flag = True
                    break
            if flag: answer = min(answer, dari(r, c, groups[r][c]))
print(answer)