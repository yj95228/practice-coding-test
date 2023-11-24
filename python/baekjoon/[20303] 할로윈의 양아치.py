import sys
input = sys.stdin.readline

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    parents[a] += parents[b]
    parents[b] = a
    arr[a] += arr[b]
    arr[b] = 0

def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

N, M, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
parents = [-1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    union(a, b)

dp = [0]*K
for x in range(1, N+1):
    if parents[x] < 0:
        V, W = arr[x], -parents[x]
        for j in range(K-1, -1, -1):
            if W <= j:
                dp[j] = max(dp[j-W]+V, dp[j])
print(dp[K-1])

# 2차 풀이
def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parents[a] += parents[b]
        parents[b] = a
        arr[a] += arr[b]

def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

N, M, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
parents = [-1 for x in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

candy = []
for x in range(1, N+1):
    if parents[x] < 0:
        candy.append((arr[x], -parents[x]))

dp = [0]*K
for v, w in candy:
    for j in range(K-1, -1, -1):
        if j >= w:
            dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])