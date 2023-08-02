# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8a04PaTowDFARO&probBoxId=AYmzaMrKU4cDFARi&type=USER&problemBoxTitle=08_230802%3A+DFS&problemBoxCnt=4
import sys

def dfs(current):
    visited[current] = 1
    # if current == 99: return 1
    for x in graph[current]:
        if not visited[x]:
            dfs(x)
            # if dfs(x): return 1
    # return 0
sys.stdin = open("input.txt", "rt")
for tc in range(1, 11):
    T, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [0]*100
    arr = list(map(int, input().split()))
    for i in range(N):
        A, B = arr[2*i:2*i+2]
        graph[A].append(B)
    dfs(0)
    print(f'#{tc} {visited[99]}')