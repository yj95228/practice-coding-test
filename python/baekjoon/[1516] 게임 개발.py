import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
rank = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
need = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)
for i in range(1, N + 1):
    time, *arr = list(map(int, input().split()))
    answer[i] = time
    for x in arr:
        if x == -1: break
        graph[x].append(i)
        need[i].append(x)
        rank[i] += 1

queue = deque()
for x in range(1, N + 1):
    if not rank[x]:
        queue.append(x)

while queue:
    x = queue.popleft()
    for u in graph[x]:
        rank[u] -= 1
        if not rank[u]:
            queue.append(u)
            answer[u] += max(map(lambda x: answer[x], need[u]))
print(*answer[1:], sep='\n')