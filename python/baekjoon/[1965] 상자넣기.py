# https://www.acmicpc.net/problem/1965
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
for x in range(1,N):
    for i in range(x):
        if arr[i] < arr[x]:
            dp[x] = max(dp[x], dp[i]+1)
print(max(dp))