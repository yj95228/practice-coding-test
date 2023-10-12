from sys import stdin
input = stdin.readline

def union(a, b):
    parents[find(b)] = find(a)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
parents = [x for x in range(N+1)]
M = int(input())
for _ in range(M):
    X, Y = map(int, input().split())
    for x in range(X,Y):
        if find(x) != find(x+1):
            union(x, x+1)
print(sum([1 for i, x in enumerate(parents[1:], start=1) if i == x]))