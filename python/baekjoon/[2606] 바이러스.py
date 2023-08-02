# https://www.acmicpc.net/problem/2606
import sys
def dfs(current):
    visited[current] = 1
    for x in graph[current]:
        if not visited[x]:
            dfs(x)
sys.setrecursionlimit(10000)    # 재귀호출 기본값 1000 => 10000
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
V = int(input())
N = int(input())
visited = [0]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
dfs(1)
print(sum(visited)-1)