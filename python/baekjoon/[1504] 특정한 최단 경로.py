from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def dijkstra(start, end):
    queue = [(0, start)]
    D = [1001*N]*(N+1)
    D[start] = 0
    while queue:
        dist, current = heappop(queue)
        if current == end: return dist
        for u, v in graph[current]:
            new_d = dist+u
            if new_d < D[v]:
                D[v] = new_d
                heappush(queue, (new_d, v))
    return -1

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))
V1, V2 = map(int, input().split())

a1, b1, c1 = dijkstra(1, V1), dijkstra(V1, V2), dijkstra(V2, N)
a2, b2, c2 = dijkstra(1, V2), dijkstra(V2, V1), dijkstra(V1, N)
if a1 == -1 or b1 == -1 or c1 == -1:
    result1 = -1
else:
    result1 = a1+b1+c1
if a2 == -1 or b2 == -1 or c2 == -1:
    result2 = -1
else:
    result2 = a2+b2+c2

if result1 == -1:
    if result2 == -1:
        print(-1)
    else:
        print(result2)
else:
    if result2 == -1:
        print(result1)
    else:
        print(min(result1, result2))