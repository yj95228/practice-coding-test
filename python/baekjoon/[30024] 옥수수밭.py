from sys import stdin
from heapq import heappop, heappush
stdin = open('input.txt','r')
input = stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
K = int(input())
arr, queue = [], []
for r in range(N):
    for c in range(M):
        if r == 0 or c == 0 or r == N-1 or c == M-1:
            heappush(queue, (-A[r][c], r, c))
            visited[r][c] = 1
answer = 0
for _ in range(K):
    result, r, c = heappop(queue)
    print(r+1, c+1)
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            heappush(queue, (-A[nx][ny], nx, ny))