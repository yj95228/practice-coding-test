# https://www.acmicpc.net/problem/1717
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def union(a,b):
    parents[find(b)] = find(a)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N, M = map(int, input().split())
parents = [x for x in range(N+1)]
for _ in range(M):
    calc, A, B = map(int, input().split())
    if calc:
        print('YES' if find(A) == find(B) else 'NO')
    else:
        union(A, B)