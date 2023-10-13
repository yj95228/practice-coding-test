# https://www.acmicpc.net/problem/29160
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

N, K = map(int, input().split())
players = [[] for _ in range(12)]
for _ in range(N):
    P, W = map(int, input().split())
    heappush(players[P], -W)

for _ in range(K):
    for p in range(1, 12):
        if not players[p]: continue
        x = heappop(players[p])
        heappush(players[p], min(0, x+1))
answer = 0
for p in range(1, 12):
    if not players[p]: continue
    answer += -players[p][0]
print(answer)