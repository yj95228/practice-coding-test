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