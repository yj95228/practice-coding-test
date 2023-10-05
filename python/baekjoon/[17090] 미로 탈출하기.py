# https://www.acmicpc.net/problem/17090
from sys import stdin
input = stdin.readline

def dfs(x,y):
    global answer, visited, can_exit
    lst = [(x,y)]
    visited[x][y] = True
    while True:
        r, c = lst[-1]
        dx, dy = dt[matrix[r][c]]
        nx, ny = r+dx, c+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            for r, c in lst:
                answer += 1
                can_exit[r][c] = True
            return
        elif visited[nx][ny]:
            if can_exit[nx][ny]:
                for r, c in lst:
                    answer += 1
                    can_exit[r][c] = True
                return
            else: return
        visited[nx][ny] = True
        lst.append((nx,ny))

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
dt = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
visited = [[False]*M for _ in range(N)]
can_exit = [[False]*M for _ in range(N)]
answer = 0
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            dfs(r,c)
print(answer)