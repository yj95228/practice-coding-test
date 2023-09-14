import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for r in range(N):
    for c in range(N):
        if dp[r][c] and matrix[r][c]:
            i = matrix[r][c]
            for dx, dy in ((1,0),(0,1)):
                nx, ny = r+i*dx, c+i*dy
                if 0 <= nx < N and 0 <= ny < N:
                    dp[nx][ny] += dp[r][c]
print(dp[N-1][N-1])