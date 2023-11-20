import sys
input = sys.stdin.readline

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return True
    if rank[a] > rank[b]:
        parents[b] = a
    else:
        parents[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def find(x):
    while parents[x]!=x:
        x = parents[x]
    return x

N, M = map(int, input().split())
parents = [x for x in range(N+1)]
rank = [0]*(N+1)
for turn in range(1, M+1):
    a, b = map(int, input().split())
    if union(a, b):
        print(turn)
        break
else: print(0)