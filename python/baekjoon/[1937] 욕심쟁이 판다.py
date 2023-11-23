import sys
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def recur(r, c):
    cnt = 1
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and A[r][c] < A[nx][ny]:
            if dp[nx][ny] == -1:
                cnt = max(cnt, recur(nx, ny)+1)
            else:
                cnt = max(cnt, dp[nx][ny]+1)
    dp[r][c] = cnt
    return cnt

N = int(input())
sys.setrecursionlimit(N*N)
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            answer = max(answer, recur(i, j))
print(answer)