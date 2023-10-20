# https://www.acmicpc.net/problem/1916
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def dijkstra(s, e):
    queue = [(0, s)]
    D = [987654321]*(N+1)
    D[s] = 0
    while queue:
        dist, current = heappop(queue)
        if current == e: return dist
        for u, v in graph[current]:
            new_d = dist+u
            if new_d < D[v]:
                D[v] = new_d
                heappush(queue, (new_d, v))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
S, E = map(int, input().split())
print(dijkstra(S, E))