# https://www.acmicpc.net/problem/11048
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    for c in range(M):
        if r > 0 and c > 0: matrix[r][c] += max(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
        elif r > 0: matrix[r][c] += matrix[r-1][c]
        elif c > 0: matrix[r][c] += matrix[r][c-1]
print(matrix[N-1][M-1])

# 더 빨리 실행되는 코드
dp = [0]*(M+1)
for i in range(1, N+1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1, M+1):
        dp[j] = max(dp[j], dp[j-1]) + arr[j]  # 사탕이 모두 양수이므로, 대각선 부분은 항상 더 작음
print(dp[M])