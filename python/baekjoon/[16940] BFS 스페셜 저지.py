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

# 2차 풀이
def solve():
    queue = [1]
    V = [0]*(N+1)
    V[1] = 1
    seq = 1
    while queue:
        next_q = []
        
        for x in queue:
            temp_q = []
            for v in graph[x]:
                if V[v]: continue
                V[v] = 1
                temp_q.append(v)
            
            for i in range(len(temp_q)):
                if arr[seq+i] in temp_q:
                    next_q.append(arr[seq+i])
                else: return 0
            seq += len(temp_q)
            
        queue = next_q
        
    return 1

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
arr = list(map(int, input().split()))

if arr[0] != 1: print(0)
else: print(solve())