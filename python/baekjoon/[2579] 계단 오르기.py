# TODO: 다시 풀어보기
# https://www.acmicpc.net/problem/2579
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
# dp[i][j] : i번째 계단에서 j번 연속 밟았을 때 최고점
dp = [[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]
print(max(dp[N][1], dp[N][2]))