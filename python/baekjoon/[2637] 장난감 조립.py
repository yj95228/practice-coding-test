import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
rank = [0] * (N + 1)
bupum = [dict() for _ in range(N + 1)]
for _ in range(M):
    x, y, k = map(int, input().split())
    graph[y].append(x)
    rank[x] += 1
    bupum[x][y] = k

queue = []
gibon = set()
for x in range(1, N + 1):
    if not rank[x]:
        queue.append(x)
        gibon.add(x)

while queue:
    next_q = []

    for x in queue:
        obj = dict()
        for k, v in bupum[x].items():
            if k in gibon:
                obj[k] = obj[k] + v if obj.get(k) else v
            else:
                for kk, vv in bupum[k].items():
                    obj[kk] = obj[kk] + v * vv if obj.get(kk) else v * vv
        bupum[x] = obj

        for v in graph[x]:
            rank[v] -= 1
            if not rank[v]:
                next_q.append(v)
    queue = next_q

for k, v in sorted(bupum[N].items(), key=lambda x: x[0]):
    print(k, v)