import sys
from heapq import heappush, heappop
from itertools import combinations
input = sys.stdin.readline

# 크루스칼
def union(a, b):
    if find(a) == find(b):
        return False
    else:
        parents[find(b)] = a
        return True

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def bfs(a, b):
    (sr, sc), (er, ec) = node[a], node[b]
    queue = [(sr, sc)]
    V = [[0]*N for _ in range(N)]
    V[sr][sc] = 1
    while queue:
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not V[nx][ny] and A[nx][ny] == '0':
                    if (nx, ny) == (er, ec): return V[r][c]
                    V[nx][ny] = V[r][c]+1
                    next_q.append((nx, ny))
        queue = next_q

def solve():
    MST = []
    for a, b in combinations(range(len(node)), 2):
        dist = bfs(a, b)
        if dist:
            MST.append((bfs(a, b), a, b))
        else:
            return -1
    MST.sort()
    key = M
    answer = 0
    for c, a, b in MST:
        if union(a, b):
            key -= 1
            if not key: return answer+c
            answer += c

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*N for _ in range(N)]
parents = [x for x in range(M+1)]
node = []
sr, sc = None, None
for r in range(1, N-1):
    for c in range(1, N-1):
        if A[r][c] in ('S', 'K'):
            A[r][c] = '0'
            node.append((r, c))
print(solve())

# 프림
def bfs(x, y):
    queue = [(x, y)]
    i = robots.index((x, y))
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    while queue:
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not visited[nx][ny] and A[nx][ny] != '1':
                    if A[nx][ny] in ('S','K'):
                        j = robots.index((nx, ny))
                        graph[i].append((visited[r][c], j))
                        graph[j].append((visited[r][c], i))
                    visited[nx][ny] = visited[r][c] + 1
                    next_q.append((nx, ny))
        queue = next_q

def prim():
    V = [0]*(M+1)
    queue = [(0, 0)]
    cnt, result = 0, 0
    while queue:
        dist, x = heappop(queue)
        if V[x]: continue
        V[x] = 1
        result += dist
        cnt += 1
        if cnt == M+1: return result
        for u, v in graph[x]:
            if V[v]: continue
            heappush(queue, (u, v))
    return -1

def solve():
    for r in range(N):
        for c in range(N):
            if A[r][c] in ('S', 'K'):
                dist = bfs(r, c)
    return prim()

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
graph = [[] for _ in range(M+1)]
robots = []
for r in range(N):
    for c in range(N):
        if A[r][c] in ('S','K'):
            robots.append((r, c))
print(solve())