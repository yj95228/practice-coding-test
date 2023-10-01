# https://www.acmicpc.net/problem/1967
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def dfs(x):
    visited = [0]*(N+1)
    visited[x] = 1
    stack = [(0,x)]
    while stack:
        d, current = stack.pop()
        for dist, v in graph[current]:
            if visited[v]: continue
            visited[v] = d+dist
            stack.append((visited[v], v))
    return max(visited)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))
answer = 0
for x in range(1,N+1):
    answer = max(answer, dfs(x))
print(0 if N == 1 else answer)