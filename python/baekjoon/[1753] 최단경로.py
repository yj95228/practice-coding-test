# TODO: 다익스트라 연습으로 다시 풀어보기 좋은 문제
# https://www.acmicpc.net/problem/1753
import sys
import heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dijkstra(c):
    distance = [11*V]*(V+1)
    distance[c] = 0
    queue = []
    heapq.heappush(queue, (distance[c], c))
    while queue:
        d, current = heapq.heappop(queue)
        if distance[current] < d: continue
        for new_d, next in graph[current]:
            if d+new_d < distance[next]:
                distance[next] = d+new_d
                heapq.heappush(queue, (d+new_d, next))
    return distance[1:]

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
for x in dijkstra(K):
    print('INF' if x == 11 else x)