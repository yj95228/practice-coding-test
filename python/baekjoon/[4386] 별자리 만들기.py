import sys
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
answer = 0
star = [list(map(float, input().split())) for _ in range(N)]
V = [0]*N
queue = [(0, 0)]
cnt = 0
while queue:
    dist, i = heappop(queue)
    if V[i]: continue
    V[i] = 1
    cnt += 1
    answer += dist
    x, y = star[i]
    if cnt == N:
        print(f'{answer:.2f}')
        break
    for j in range(N):
        if i == j: continue
        xx, yy = star[j]
        heappush(queue, (((x-xx)**2+(y-yy)**2)**(1/2), j))