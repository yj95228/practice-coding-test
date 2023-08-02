# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8WIEr6A8IDFARO&probBoxId=AYmuRN-KAGwDFARi&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=9
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    answer = []
    for _ in range(E):
        v, e = map(int, input().split())
        graph[v].append(e)
        graph[e].append(v)
    stack = [1]
    while stack:
        v = stack.pop(0)
        if not visited[v]:
            visited[v] = True
            answer.append(v)
            stack = sorted(graph[v]) + stack
    print(f'#{tc}', *answer)

# 강사님 코드
# for tc in range(1,T+1):
#     V, E = map(int, input().split())
#
#     # (1) 인접리스트에 저장
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         s, e = map(int, input().split())
#         graph[s].append(e)
#         graph[e].append(s)  # 양방향 간선이므로
#
#     for x in graph:
#         x.sort()
#
#     # (2) 깊이 우선 탐색
#     answer, stack = [], []
#     visited = [False for _ in range(V + 1)]
#
#     current = 1
#     visited[current] = True
#     answer.append(current)
#
#     while True:
#         for next in graph[current]:
#             if not visited[next]:
#                 stack.append(current)   #되돌아오기 위해
#
#                 current = next
#                 visited[current] = 1
#                 answer.append(current)
#                 break   # 기준점이 c(n)으로 바뀌므로 더 이상 탐색할 곳 없음
#         else:
#             if stack:
#                 current = stack.pop()
#             else:
#                 break
#     print(f'#{tc}', *answer)

# 재귀로 풀기
def dfs(current):
    # [1] 방문 표시, 첫 방문 시 해야할 일
    visited[current] = True
    answer.append(current)
    # [2] 연결된 4/8 방향 등 반복 처리
    # 범위 이내, 미방문 시, ** 조건에 맞으면 방문(dfs호출)
    for x in graph[current]:
        if not visited[x]:  # 방문하지 않은 경우
            dfs(x)


visited = [0]*(V+1)
answer = []
dfs(1)  # 첫 위치만 방문, main 루프에서는 가장 위 한번만 호출
print(f'#{tc}', *answer)