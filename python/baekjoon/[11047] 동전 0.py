# https://www.acmicpc.net/problem/11047

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
answer = 0
for i in range(N):
  coins.append(int(input()))
coins = sorted(coins, reverse=True)
while K:
  for coin in coins:
    a, b = divmod(K,coin)
    answer += a
    K = b
print(answer)