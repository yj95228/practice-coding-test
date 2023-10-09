# https://www.acmicpc.net/problem/1922
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
MST = []
answer, cnt = 0, 0
for _ in range(M):
    A, B, C = map(int, input().split())
    MST.append((A, B, C))
MST.sort(key=lambda x: x[2])
for a, b, c in MST:
    if cnt == N-1: break
    if find(a) != find(b):
        union(a, b)
        answer += c
        cnt += 1
print(answer)