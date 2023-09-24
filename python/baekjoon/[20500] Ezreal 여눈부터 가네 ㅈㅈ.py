# https://www.acmicpc.net/problem/20500

import sys
input = sys.stdin.readline

N = int(input())
dp = [0,0]
for x in range(1,N):
    if x%2:
        dp.append((dp[-1]*2+1)%1_000_000_007)
    else:
        dp.append((dp[-1]*2-1)%1_000_000_007)
print(dp[-1])