# https://www.acmicpc.net/problem/13023
# BFS로는 풀 수 없는 문제
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(current, cnt):
    if cnt == 5: return True
    for x in graph[current]:
        if not visited[x]:
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

# answer 변수를 추가해서 빨리 종료시키기
def dfs(current, cnt):
    global answer
    if answer: return
    if cnt == 5:
        answer = 1
        return
    for x in graph[current]:
        if not visited[x]:
            visited[x] = True
            if dfs(x, cnt+1): return 1
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
answer = 0
solve()
print(answer)