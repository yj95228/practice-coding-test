# 1번째만에 성공 / 풀이 시간: 30분 소요 / 117504kb / 456ms
# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(n, start, arr):
    global answer
    if n == 3:
        result = cnt
        visited = [[False]*(M+2) for _ in range(N+2)]
        queue = deque([])

        for r, c in virus:
            queue.append((r,c))
            visited[r][c] = True

        for r, c in arr:
            visited[r][c] = True
            result -= 1

        while queue:
            r,c = queue.popleft()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not visited[nx][ny] and matrix[nx][ny] == '0':
                    visited[nx][ny] = True
                    result -= 1
                    queue.append((nx,ny))
        answer = max(result, answer)
        return

    for i in range(start, cnt):
        x, y = safe_area[i]
        matrix[x][y] = '1'
        dfs(n+1, i+1, arr+[safe_area[i]])
        matrix[x][y] = '0'

N, M = map(int, input().split())
matrix = [['1']*(M+2)] + [['1'] + input().split() + ['1'] for _ in range(N)] + [['1']*(M+2)]
virus = []
safe_area = []
answer, cnt = 0, 0

for r in range(1,N+1):
    for c in range(1,M+1):
        if matrix[r][c] == '2':
            virus.append((r,c))
        elif matrix[r][c] == '0':
            safe_area.append((r,c))
            cnt += 1

dfs(0, 0, [])
print(answer)