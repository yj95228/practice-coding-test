# TODO: 벽 부수는 경우와 아닌 경우 visited 관리 따로
# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[[False]*M for _ in range(N)] for _ in range(2)]
queue = deque([(False, 1, 0, 0)])
visited[False][0][0] = True

while queue:
    wall, cnt, r, c = queue.popleft()
    if (r,c) == (N-1, M-1):
        print(cnt)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        if 0 <= r+dx < N and 0 <= c+dy < M and not visited[wall][r+dx][c+dy]:
            if wall and matrix[r+dx][c+dy] == '1': continue
            queue.append((wall or matrix[r+dx][c+dy] == '1', cnt+1, r+dx, c+dy))
            visited[wall][r+dx][c+dy] = True
else: print(-1)