import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(x):
    global answer
    queue = [(0, x)]
    D = [987654321]*(N+1)
    D[x] = 0
    item = set()
    while queue:
        dist, current = heappop(queue)
        if dist <= M:
            item.add(current)
        else: break
        for u, v in graph[current]:
            new_d = dist+u
            if new_d < D[v]:
                D[v] = new_d
                heappush(queue, (new_d, v))
    
    answer = max(answer, sum(arr[x] for x in item))

N, M, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(K):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

answer = 0
for x in range(1, N+1):
    dijkstra(x)
print(answer)