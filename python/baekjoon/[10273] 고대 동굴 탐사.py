import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    rank = [0]*(N+1)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        rank[b] += 1

    V = [0]*(N+1)
    D = [-10001*N]*(N+1)
    D[1] = arr[1]
    queue = deque([(1, 1)])
    mx, answer, last = -10001*N, 1, 1
    while queue:
        x, cnt = queue.popleft()
        if mx < D[x]:
            mx, answer, last = D[x], cnt, x
        for cost, next in graph[x]:
            rank[next] -= 1
            D[next] = max(D[next], D[x]+arr[next]-cost)
            if not rank[next]:
                V[next] = x
                queue.append((next, cnt+1))
    print(mx, answer)

    start = last
    answer = deque()
    while True:
        if not start: break
        answer.appendleft(start)
        start = V[start]
    print(*answer)