import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [*matrix[0], *matrix[0]]
for r in range(1,N):
    answer = [*matrix[r], *matrix[r]]
    answer[0] += min(dp[:2])
    answer[1] += min(dp[:3])
    answer[2] += min(dp[1:3])
    answer[3] += max(dp[3:5])
    answer[4] += max(dp[3:])
    answer[5] += max(dp[4:])
    dp = answer
print(max(dp), min(dp))