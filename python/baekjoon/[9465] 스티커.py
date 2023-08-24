# https://www.acmicpc.net/problem/9465
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = list(map(list, zip([0]*N, *arr)))
    for i in range(1,N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2])
        dp[i][2] += max(dp[i-1][0], dp[i-1][1])
    print(max(dp[-1]))