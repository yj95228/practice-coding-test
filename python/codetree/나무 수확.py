N = int(input())
A = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(2)]
dp[0][1][1] = A[1][1]
dp[1][1][1] = A[1][1]*2
for r in range(1, N+1):
    for c in range(1, N+1):
        dp[1][r][c] = max(dp[0][r][c-1], dp[0][r-1][c]) + A[r][c]*2
        for k in range(2):
            candidate = max(dp[k][r-1][c], dp[k][r][c-1]) + A[r][c]
            dp[k][r][c] = max(dp[k][r][c], candidate)
print(dp[1][N][N])