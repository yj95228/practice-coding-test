# https://www.acmicpc.net/problem/17396
from sys import stdin
from heapq import heappop, heappush
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

N, M = map(int, input().split())
siya = input().split()
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((T,B))
    graph[B].append((T,A))
    
distance = [100000*N]*N
distance[0] = 0
queue = [(0,0)]

while queue:
    time, current = heappop(queue)
    
    if current == N-1:
        print(time)
        break
    elif time > distance[current]: continue
        
    for u, v in graph[current]:
        dist = time+u
        if (v == N-1 or siya[v] == '0') and dist < distance[v]:
            distance[v] = dist
            heappush(queue, (dist, v))
            
else: print(-1)