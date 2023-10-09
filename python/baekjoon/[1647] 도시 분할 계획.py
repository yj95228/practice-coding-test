# https://www.acmicpc.net/problem/1647
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def union(a, b):
    parents[find(a)] = find(b)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N, M = map(int, input().split())
parents = [x for x in range(N+1)]
MST = []
for _ in range(M):
    A, B, C = map(int, input().split())
    MST.append((C, A, B))
MST.sort()
answer, cnt = 0, 0
for c, a, b in MST:
    if cnt == N-2: break
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        answer += c
print(answer)