# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8azJnaTfMDFARO&probBoxId=AYmzaMrKU4cDFARi&type=USER&problemBoxTitle=08_230802%3A+DFS&problemBoxCnt=4
import sys

def dfs(current):
    visited[current] = True # 1
    for x in graph[current]:
        if not visited[x]:
            dfs(x)

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)] # [0]*(V+1)
    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
    S, G = map(int, input().split())
    dfs(S)
    print(f'#{tc} {1 if visited[G] else 0}') # return visited[G]