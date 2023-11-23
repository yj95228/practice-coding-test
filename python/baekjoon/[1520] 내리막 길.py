# TODO: 답 보고 풀었음
# https://www.acmicpc.net/problem/1520
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(r,c):
    if (r,c) == (M,N): return 1
    if dp[r][c] != -1: return dp[r][c]
    dp[r][c] = 0
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if matrix[r][c] > matrix[nx][ny]:
            dp[r][c] += dfs(nx,ny)
    return dp[r][c]

M, N = map(int, input().split())
matrix = [[10001]*(N+2)] +\
         [[10001] + list(map(int, input().split())) + [10001] for _ in range(M)] +\
         [[10001]*(N+2)]
dp = [[-1]*(N+2) for _ in range(M+2)]
print(dfs(1,1))

# 다시 풀기
def recur(r, c, num):
    if (r, c) == (N-1, M-1): return 1
    cnt = 0
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and num > A[nx][ny]:
            if dp[nx][ny] == -1:
                cnt += recur(nx, ny, A[nx][ny])
            else:
                cnt += dp[nx][ny]
    dp[r][c] = cnt
    return cnt

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
recur(0, 0, A[0][0])
print(dp[0][0])