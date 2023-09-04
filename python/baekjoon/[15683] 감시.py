# FIXME: 새로 감시하게 된 영역을 따로 저장하여 재귀 및 visited 배열 복구
# https://www.acmicpc.net/problem/15683
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(n):
    global answer
    if n == cnt:
        answer = min(answer, sum(len(x) == 0 for row in visited[1:N+1] for x in row[1:M+1]))
        return
    type, r, c = cctv[n]
    visited[r][c].add(n)
    for case in dt[type]:
        for dx, dy in case:
            i, nx, ny = 1, r+dx, c+dy
            while 10 not in visited[nx][ny]:
                visited[nx][ny].add(n)
                i += 1
                nx, ny = r+dx*i, c+dy*i
        dfs(n+1)
        for dx, dy in case:
            i, nx, ny = 1, r+dx, c+dy
            while n in visited[nx][ny]:
                visited[nx][ny].remove(n)
                i += 1
                nx, ny = r+dx*i, c+dy*i

N, M = map(int, input().split())
matrix = [[6]*(M+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6]*(M+2)]
visited = [[set() for _ in range(M+2)] for _ in range(N+2)]
cctv, cnt = [], 0
dt = [
    [],
    [[[1,0]],[[0,1]],[[-1,0]],[[0,-1]]],
    [[[1,0],[-1,0]], [[0,1],[0,-1]]],
    [[[1,0],[0,1]], [[0,1],[-1,0]], [[-1,0],[0,-1]], [[0,-1],[1,0]]],
    [[[1,0],[0,1],[-1,0]], [[1,0],[0,1],[0,-1]], [[1,0],[-1,0],[0,-1]], [[0,1],[-1,0],[0,-1]]],
    [[[1,0],[0,1],[-1,0],[0,-1]]]
]
for r in range(N+2):
    for c in range(M+2):
        if 0 < matrix[r][c] < 6:
            cnt += 1
            cctv.append((matrix[r][c],r,c))
        elif matrix[r][c] == 6:
            visited[r][c].add(10)
answer = N*M
dfs(0)
print(answer)