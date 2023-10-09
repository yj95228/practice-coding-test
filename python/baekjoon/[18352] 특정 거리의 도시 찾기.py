# https://www.acmicpc.net/problem/18352
from sys import stdin
from collections import deque
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
distance = [987654321]*(N+1)
distance[X] = 0
queue = deque([X])
while queue:
    current = queue.popleft()
    for x in graph[current]:
        if distance[current]+1 < distance[x]:
            distance[x] = distance[current]+1
            queue.append(x)
exist = False
for i, x in enumerate(distance[1:], start=1):
    if x == K:
        exist = True
        print(i)
if not exist: print(-1)