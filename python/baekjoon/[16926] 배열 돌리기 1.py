# TODO: 굉장히 더럽게 풀었음
# https://www.acmicpc.net/problem/16926
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, R = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
visited1 = [[False]*M for _ in range(N)]
visited2 = [[False]*M for _ in range(N)]
i, d, L = 0, 0, min(N//2,M//2)
dt = ((0,1),(1,0),(0,-1),(-1,0))

for _ in range(L):
    r, c = i, i
    arr = deque([matrix[r][c]])
    while True:
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if (nx,ny) == (i,i):
            for _ in range(R):
                arr.append(arr.popleft())
            r, c, d = i+1, i, 3
            for x in arr:
                dx2, dy2 = dt[d]
                nx2, ny2 = r+dx2, c+dy2
                if not (0 <= nx2 < N and 0 <= ny2 < M) or visited2[nx2][ny2]:
                    d = (d+1)%4
                    dx2, dy2 = dt[d]
                    nx2, ny2 = r+dx2, c+dy2
                visited2[nx2][ny2] = True
                matrix[nx2][ny2] = x
                r, c = nx2, ny2
            break
        elif 0 <= nx < N and 0 <= ny < M and not visited1[nx][ny]:
            visited1[nx][ny] = True
            arr.append(matrix[nx][ny])
            r, c = nx, ny
        else: d = (d+1)%4
    i += 1
    visited1 = [v[:] for v in visited2]

for row in matrix:
    print(*row)