# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8rgNWqVnoDFAQe&probBoxId=AYm4kJEa4c4DFARi+&type=USER&problemBoxTitle=09_230803%3A+Queue_BFS&problemBoxCnt=++5+
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    answer = []
    for _ in range(E):
        v, e = map(int, input().split())
        graph[v].append(e)
        graph[e].append(v)
    queue = [1]
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = True
            answer.append(v)
            queue = queue + sorted(graph[v])
    print(f'#{tc}', *answer)


# 강사님 코드
def bfs(current):
    #[0] queue, visited, 필요한 변수 선언(생성)
    queue = []
    visited = [0]*(N+1)

    #[1] queue에 초기 데이터(들) 삽입, visited 표시
    queue.append(current)
    visited[current] = 1

    #[2] queue에 데이터가 있는 동안 반복 처리
    while queue:
        current = queue.pop(0)  # 큐에서 데이터 한 개 꺼냄

        # 연결, 4/8방향 반복처리
        # 범위내, 미방문, ** 조건에 맞으면
        for x in graph[current]:
            if visited[current] == 0:
                queue.append(x)
                visited[x] = 1
                answer.append(x)

# bfs 함수 따로 빼는 방법
def bfs(c):
    # [0] queue, visited, 필요한 변수 선언(생성)
    queue = []

    # [1] queue에 초기데이터(들) 삽입, visited[]표시, 첫 방문시 처리
    queue.append(current)
    visited[current] = 1
    answer.append(current)

    # [2] queue에 데이터가 있는동안 반복처리
    while queue:
        current = queue.pop(0)  # 큐에서 데이터 한 개 꺼냄

        # 연결, 4/8방향 반복처리
        # 범위내, 미방문, **조건에 맞으면
        for x in graph[current]:
            if visited[x] == 0:
                queue.append(x)
                visited[x] = visited[current] + 1
                answer.append(x)