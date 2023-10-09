# https://www.acmicpc.net/problem/16236
from sys import stdin
input = stdin.readline

def dfs(x, y):
    result = 0
    visited = [[0]*(M+2) for _ in range(N+2)]
    visited[x][y] = 1
    stack = [(x, y)]
    lst = [(x, y)]
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if visited[nx][ny] or narr[nx][ny] == '1': continue
            elif narr[nx][ny] == '0': return 0
            else:
                visited[nx][ny] = 1
                lst.append((nx, ny))
                stack.append((nx, ny))
    for r, c in lst:
        narr[r][c] = '1'
        result += 1
    return result

N, M = map(int, input().split())
matrix = [['1']*(M+2)] + [['1'] + input().split() + ['1'] for _ in range(N)] + [['1']*(M+2)]
can = []
for r in range(1,N+1):
    for c in range(1,M+1):
        if matrix[r][c] == '0':
            can.append((r,c))
length = len(can)
answer = 0
for i in range(length-1):
    for j in range(i+1, length):
        narr = [row[:] for row in matrix]
        (k, l), (m, n) = can[i], can[j]
        narr[k][l], narr[m][n] = '1', '1'
        result = 0
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = k+dx, l+dy
            if narr[nx][ny] == '2':
                result += dfs(nx, ny)
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = m+dx, n+dy
            if narr[nx][ny] == '2':
                result += dfs(nx, ny)
        answer = max(result, answer)
print(answer)