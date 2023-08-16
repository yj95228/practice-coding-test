# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX_aA_HqDwUDFAVy&probBoxId=AYn7aaSaYAgDFARi+&type=USER&problemBoxTitle=17_230816%3A+%EA%B7%B8%EB%9E%98%ED%94%84%ED%99%9C%EC%9A%A9&problemBoxCnt=++4+
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    INF = 10*N
    matrix = [[INF]*N for _ in range(N)]
    visited = [False]*N
    for _ in range(E):
        start, end, weight = map(int, input().split())
        matrix[start][end] = weight
        if start == 0:
            visited[end] = True
    for v in range(N):
        matrix[v][v] = 0
    visited[0] = True
    while not visited[N-1]:
        j = matrix[0].index(INF)
        for i, x in enumerate(matrix[0]):
            if x == INF: continue
            matrix[0][j] = min(matrix[0][j], matrix[0][i]+matrix[i][j])
            visited[j] = True
    print(f'#{tc} {matrix[0][N-1]}')

# TODO: 다익스트라 알고리즘 공부하기
def dijkstra(start, end):
    D = adj[start][::]      # 시작 위치에 해당하는 D[] 복사
    visited = [False]*N     # 최단 경로를 확정한 노드 표시
    visited[start] = True   # 시작 노드에서 출발

    for _ in range(N-1):    # N-1개 노드에 대한 최단경로 설정
        # [1] 미방문 노드 중 최단거리 노드(시작노드 기준) 찾기 : D[]에서 찾기
        idx, mn = -1, INF
        for i in range(N):
            if not visited[i] and D[i] < mn:
                idx, mn = i, D[i]
        visited[idx] = True # idx 선택, 최단거리 선택 완료 표시

        # [2] 선택노드(idx)를 경유하는 경우와 현재 비용 중 최솟값으로 갱신 : D[]
        for j in range(N):
            if not visited[j]:
                D[j] = min(D[j], D[idx] + adj[idx][j])
    return D[end]           # 목적지까지의 최소비용

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    INF = 10*N
    D = [[INF]*N for _ in range(N)]

    # [1] 인접행렬에 가중치 저장
    adj = [[INF]*N for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
    for _ in range(E):
        S, E, W = map(int, input().split())
        adj[S][E] = W

    answer = dijkstra(0, N-1)
    print(f'#{tc} {answer}')