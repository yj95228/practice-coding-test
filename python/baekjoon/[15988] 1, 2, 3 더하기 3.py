# https://www.acmicpc.net/problem/12101
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())
dp = [1,2,4]
for _ in range(T):
    N = int(input())
    while len(dp) < N:
        dp.append((dp[-3]+dp[-2]+dp[-1])%1_000_000_009)
    print(dp[N-1])