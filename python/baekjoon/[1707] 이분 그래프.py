import sys
input = sys.stdin.readline

def bfs(x):
    queue = [(1, x)]
    visited[x] = 1
    while queue:
        next_q = []
        for color, x in queue:
            for u in graph[x]:
                if visited[u] == -1:
                    visited[u] = 1-color
                    next_q.append((1-color, u))
                elif visited[u] == color:
                    return True
        queue = next_q
    return False

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1]*(V+1)
    for x in range(1, V+1):
        if visited[x] == -1:
            if bfs(x):
                print('NO')
                break
    else: print('YES')