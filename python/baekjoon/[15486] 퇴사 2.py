# https://www.acmicpc.net/problem/3190
from sys import stdin
from collections import deque
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)
mx = 0
for x in range(N):
    T, P = arr[x]
    mx = max(mx, dp[x])
    if x+T <= N:
        dp[x+T] = max(mx+P, dp[x+T])
print(max(dp))