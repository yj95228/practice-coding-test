import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(1, T+1):
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    rank = [0]*(N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        rank[Y] += 1

    W = int(input())
    V = [0]*(N+1)
    dp = [0]*(N+1)
    queue = deque()
    for x in range(1, N+1):
        if rank[x] == 0:
            queue.append((arr[x], x))
            V[x] = 1
            dp[x] = arr[x]

    while queue:
        mx = 0
        for _ in range(len(queue)):
            time, x = queue.popleft()
            for v in graph[x]:
                dp[v] = max(dp[v], dp[x]+arr[v])
                if V[v]: continue
                rank[v] -= 1
                if rank[v] == 0:
                    V[v] = 1
                    queue.append((arr[v], v))
    print(dp[W])