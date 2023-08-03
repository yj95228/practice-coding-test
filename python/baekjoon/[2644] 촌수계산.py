# https://www.acmicpc.net/problem/2644
import sys

def bfs(A):
    queue = [A]
    while queue:
        current = queue.pop()
        if current == B: return chon[current]
        for x in graph[current]:
            if not chon[x]:
                chon[x] += chon[current] + 1
                queue.append(x)

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
chon = [0]*(N+1)
M = int(input())
for _ in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)
print(bfs(A) or -1)