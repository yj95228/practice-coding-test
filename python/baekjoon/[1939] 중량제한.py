import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
mx = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((-C, B))
    graph[B].append((-C, A))
    mx = max(mx, C)
A, B = map(int, input().split())
D = [0]*(N+1)
answer = 0
queue = [(-mx, A)]
while queue:
    weight, current = heappop(queue)
    if current == B:
        print(-weight)
        break
    for u, v in graph[current]:
        new_d = max(weight, u)
        if new_d < D[v]:
            D[v] = new_d
            heappush(queue, (new_d, v))