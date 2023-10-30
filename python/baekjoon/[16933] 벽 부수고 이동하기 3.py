# https://www.acmicpc.net/problem/16933
from sys import stdin
from collections import deque
stdin = open('input.txt','r')
input = stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
V = [[K]*M for _ in range(N)]
V[0][0] -= 1
queue = deque([(1, 0, 0, 0)])
while queue:
    time, wall, r, c = queue.popleft()
    if (r, c) == (N-1, M-1):
        print(time)
        break
    if time%2:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and wall <= V[nx][ny]:
                V[nx][ny] -= 1
                if A[nx][ny]:
                    queue.append((time+1, wall+1, nx, ny))
                else:
                    queue.append((time+1, wall, nx, ny))
    else:
        queue.append((time+1, wall, r, c))
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and wall <= V[nx][ny] and not A[nx][ny]:
                V[nx][ny] -= 1
                queue.append((time+1, wall, nx, ny))
else: print(-1)