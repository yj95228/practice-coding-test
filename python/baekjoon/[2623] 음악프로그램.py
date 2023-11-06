import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
rank = [0]*(N+1)
for _ in range(M):
    K, *arr = list(map(int, input().split()))
    for x in range(K-1):
        A, B = arr[x], arr[x+1]
        graph[A].append(B)
        rank[B] += 1

queue = deque()
for x in range(1, N+1):
    if rank[x] == 0:
        queue.append(x)

answer = []
while queue:
    x = queue.popleft()
    answer.append(x)
    for v in graph[x]:
        rank[v] -= 1
        if rank[v] == 0:
            queue.append(v)
if len(answer) == N:
    print(*answer, sep='\n')
else: print(0)