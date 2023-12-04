import sys
input = sys.stdin.readline

def solve():
    V = [0]*(N+1)
    visited = [0]*M
    V[1] = 1
    queue = [1]
    turn = 1
    while queue:
        temp_q = []
        for x in queue:
            if x == N: return turn
            for h in graph[x]:
                if visited[h]: continue
                visited[h] = 1
                for v in hyper[h]:
                    if V[v]: continue
                    V[v] = 1
                    temp_q.append(v)
        turn += 1
        queue = temp_q
    return -1

N, K, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
hyper = [[] for _ in range(M)]
for idx in range(M):
    arr = list(map(int, input().split()))
    hyper[idx] = arr
    for x in arr:
        graph[x].append(idx)
print(solve())