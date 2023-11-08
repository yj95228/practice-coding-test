import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def union(a, b):
    parents[find(b)] = find(a)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
M = int(input())
parents = [x for x in range(N+1)]
A = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))
for i in range(2, N+1):
    for j in range(1, i):
        if A[i][j]:
            union(i, j)

for x in range(1, M):
    if find(arr[x]) != find(arr[x-1]):
        print('NO')
        break
else: print('YES')