# https://www.acmicpc.net/problem/16940
from sys import stdin
from collections import deque
input = stdin.readline

def solve():
    queue = deque([1])
    visited = [0]*(N+1)
    visited[1] = 1
    idx = 1
    while queue:
        v = queue.popleft()
        if seq[v] != idx: return 0
        idx += 1

        q = []
        for x in graph[v]:
            if visited[x]: continue
            visited[x] = 1
            q.append((seq[x], x))
        q.sort()

        for i in range(len(q)):
            queue.append(q[i][1])

    return 1

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
check = [0] + list(map(int, input().split()))

seq = [0]*(N+1)
for i in range(1,N+1):
    seq[check[i]] = i
print(solve())