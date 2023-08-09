# https://www.acmicpc.net/problem/13023
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(current, cnt):
    if cnt == 5: return True
    for x in graph[current]:
        if not visited[x]:
            print(current, x, cnt, visited)
            visited[x] = True
            if dfs(x, cnt+1): return True
            visited[x] = False

def solve():
    for i in range(N):
        visited[i] = True
        if dfs(i,1): return 1
        visited[i] = False

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False]*N
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
print(solve() or 0)