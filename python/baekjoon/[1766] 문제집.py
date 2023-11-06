import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
rank = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    rank[B] += 1

queue = []
for x in range(1, N+1):
    if rank[x] == 0:
        heappush(queue, x)

answer = []
while queue:
    x = heappop(queue)
    answer.append(x)
    for v in graph[x]:
        rank[v] -= 1
        if rank[v] == 0:
            heappush(queue, v)
print(*answer)