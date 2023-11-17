import sys
input = sys.stdin.readline

graph = [[] for _ in range(10001)]
while True:
    try:
        A, B, C = map(int, input().split())
        graph[A].append((C, B))
        graph[B].append((C, A))
    except:
        queue = [(0, 1)]
        V = [0]*10001
        D = [0]*10001
        V[1] = 1
        while queue:
            next_q = []
            for d, x in queue:
                for dd, next in graph[x]:
                    if V[next]: continue
                    V[next] = 1
                    D[next] = d+dd
                    next_q.append((d+dd, next))
            queue = next_q
        mx = max(D)
        idx = D.index(mx)
        queue = [(0, idx)]
        V = [0]*10001
        V[idx] = 1
        D = [0]*10001
        while queue:
            next_q = []
            for d, x in queue:
                for dd, next in graph[x]:
                    if V[next]: continue
                    V[next] = 1
                    D[next] = d + dd
                    next_q.append((d + dd, next))
            queue = next_q
        print(max(D))
        break