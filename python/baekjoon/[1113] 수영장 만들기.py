import sys
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(x, y):
    V[x][y] = 1
    queue = [(x, y)]
    cnt = 1
    flag = True
    while queue:
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M:
                    if not V[nx][ny] and B[nx][ny] > 0:
                        cnt += 1
                        V[nx][ny] = 1
                        next_q.append((nx, ny))
                else: flag = False
        queue = next_q
    return cnt if flag else 0

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0
for x in range(2, 10):
    B = [[x-A[r][c] for c in range(M)] for r in range(N)]
    V = [[0] * M for _ in range(N)]
    for r in range(1, N-1):
        for c in range(1, M-1):
            if not V[r][c] and B[r][c] > 0:
                answer += bfs(r, c)
print(answer)