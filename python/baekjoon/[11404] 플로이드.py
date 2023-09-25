import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt','r')

def dijkstra(x):
    D = distance[x]
    visited = [False]*(N+1)
    visited[x] = True
    queue = [(0, x)]
    while queue:
        d, current = heappop(queue)
        if D[current] < d: continue
        for w, v in graph[current]:
            new_d = w+d
            if D[v] < new_d: continue
            D[v] = new_d
            heappush(queue, (new_d, v))
    return list(map(lambda x: 0 if x == 100001*N else x, D[1:]))

N = int(input())
graph = [[] for _ in range(N+1)]
distance = [[100001*N]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i] = 0

M = int(input())
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C,B))
    distance[A][B] = C

for x in range(1,N+1):
    print(*dijkstra(x))
