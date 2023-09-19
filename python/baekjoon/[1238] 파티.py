# TODO: 다시 풀어보기
# https://www.acmicpc.net/problem/1238
import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dijkstra(start, end):
    queue = []
    heappush(queue, (0, start))
    visited = distance[start]
    while queue:
        d, current = heappop(queue)
        if visited[current] < d: continue
        for w, v in graph[current]:
            if visited[current] + w < visited[v]:
                visited[v] = visited[current] + w
                heappush(queue, (visited[v], v))
    return visited[end]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((T,B))

distance = [[987654321]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i] = 0

print(max([dijkstra(i,X)+dijkstra(X,i) for i in range(1,N+1)]))