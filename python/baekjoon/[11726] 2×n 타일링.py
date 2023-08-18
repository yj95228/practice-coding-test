# https://www.acmicpc.net/problem/11726
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
dp = [1,1]
if N == 1: print(1)
else:
    for x in range(1,N+1):
        dp.append((dp[x]+dp[x-1])%10007)
    print(dp[N])