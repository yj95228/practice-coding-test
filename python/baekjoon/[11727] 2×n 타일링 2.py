# https://www.acmicpc.net/problem/11727
import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
N = int(input())
dp = [0,1]
for x in range(2,N//2+2):
    dp.append(dp[-1]*2+1)
    dp.append(dp[-1]*2-1)
print(dp[N]%10007)

# 다른 점화식
dp = [0,1,3]
for x in range(3,N+1):
    dp.append(dp[-2]*2+dp[-1])
print(dp[N]%10007)