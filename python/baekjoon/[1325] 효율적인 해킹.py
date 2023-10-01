# https://www.acmicpc.net/problem/1325
# 1차 시도: visited[x] = visited[v]+1로 cnt해줌
# 2차 시도: graph에 여러 개 연결되어있을 경우 둘다 +1 되지 않으므로 영역 구하기처럼 각각 +1 처리
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
cnt = [0]*(N+1)

for n in range(1,N+1):
    visited = [False]*(N+1)
    visited[n] = True
    stack = [n]
    
    while stack:
        v = stack.pop()
        cnt[n] += 1
        
        for x in graph[v]:
            if not visited[x]:
                visited[x] = True
                stack.append(x)
                
mx = max(cnt[1:])
print(*[i+1 for i, x in enumerate(cnt[1:]) if x == mx])