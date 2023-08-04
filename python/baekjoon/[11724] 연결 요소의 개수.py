# https://www.acmicpc.net/problem/11724
import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for x in range(1,N+1):
    if not visited[x]:
        queue = [x]
        answer += 1
        visited[x] = True
        while queue:
            x = queue.pop(0)
            for v in graph[x]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
print(answer)