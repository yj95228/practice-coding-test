# https://www.acmicpc.net/problem/11725
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
root = [1]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque([1])
visited = [False]*(N+1)
visited[1] = True
while queue:
    v = queue.popleft()
    for x in graph[v]:
        if not visited[x]:
            root[x] = v
            visited[x] = True
            queue.append(x)
print(*root[2:], sep='\n')