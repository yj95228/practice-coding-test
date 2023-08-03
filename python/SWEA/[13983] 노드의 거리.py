# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX805keq15EDFAQe&probBoxId=AYm4kJEa4c4DFARi&type=USER&problemBoxTitle=09_230803%3A+Queue_BFS&problemBoxCnt=5
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    distance = [0]*(V+1)
    for _ in range(E):
        v, e = map(int, input().split())
        graph[v].append(e)
        graph[e].append(v)
    S, G = map(int, input().split())

    queue = [S]
    while queue:
        current = queue.pop(0)
        for x in graph[current]:
            if not distance[x]:
                queue.append(x)
                distance[x] = distance[current] + 1

    print(f'#{tc} {distance[G]}')