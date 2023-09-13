# 1차 제출: 시간 초과
# 2차 제출: 대각선 가지치기 추가
# 3차 제출: 범위 체크 안 하게 패딩
# 4차 제출: 가지치기 N+1 -> N
# 5차 제출: dp로 풀었음

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
matrix = [input().split() for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

for r in range(N):
    for c in range(1,N):
        if matrix[r][c] == '0':
            if matrix[r][c-1] == '0':
                dp[0][r][c] += dp[0][r][c-1] + dp[2][r][c-1]
            if matrix[r-1][c] == '0':
                dp[1][r][c] += dp[1][r-1][c] + dp[2][r-1][c]
            if matrix[r][c-1] == '0' and matrix[r-1][c] == '0':
                dp[2][r][c] += dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])