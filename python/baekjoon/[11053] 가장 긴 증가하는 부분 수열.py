# TODO: 문제를 잘못 이해했어서 푸는데 오래 걸렸음
# dp 테이블 초기화를 0이 아닌 1로 했어야
# https://www.acmicpc.net/problem/11727
import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
for x in range(1,N):
    for i in range(x):
        if arr[i] < arr[x]:
            dp[x] = max(dp[x], dp[i]+1)
print(max(dp))

# 더 짧게
dp = [0] * 1001
for x in arr:
    dp[x] = max(arr[:x]) + 1
print(max(dp))