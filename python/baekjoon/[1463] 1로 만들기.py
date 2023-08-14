# https://www.acmicpc.net/problem/1463
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(x, cnt):
    global answer
    if cnt > answer: return
    if x == 1:
        answer = min(answer, cnt)
        return
    if x%3 == 0: dfs(x//3, cnt+1)
    if x%2 == 0: dfs(x//2, cnt+1)
    dfs(x-1, cnt+1)
N = int(input())
answer = pow(10,6)
dfs(N,0)
print(answer)

# DP로 풀기
N = int(input())
dp = [0]*(N+1)
for x in range(2,N+1):
    if x%6 == 0: dp[x] = min(dp[x//2]+1, dp[x//3]+1, dp[x-1]+1)
    elif x%3 == 0: dp[x] = min(dp[x//3]+1, dp[x-1]+1)
    elif x%2 == 0: dp[x] = min(dp[x//2]+1, dp[x-1]+1)
    else: dp[x] = dp[x-1]+1
print(dp[N])

# 더 짧게
for x in range(2,N+1):
    dp[x] = dp[x-1]+1
    if x%3 == 0: dp[x] = min(dp[x//3]+1, dp[x])
    if x%2 == 0: dp[x] = min(dp[x//2]+1, dp[x])
print(dp[N])