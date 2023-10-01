# https://www.acmicpc.net/problem/1309
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N = int(input())
dp = [1,3]
for x in range(2,N+1):
    dp.append((dp[-1]*2+dp[-2])%9901)
print(dp[N])
