from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) + [1]*K for _ in range(2)]
visited = [[0]*(N+K) for _ in range(2)]
queue = deque([(0, 0, 0)])
visited[0][0] = 1
while queue:
    time, r, c = queue.popleft()
    if c >= N:
        print(1)
        break
    if c+1 < N+K and not visited[r][c+1] and A[r][c+1] and time+1 <= c+1:
        visited[r][c+1] = 1
        queue.append((time+1, r, c+1))
    if 0 <= c-1 and not visited[r][c-1] and A[r][c-1] and time+1 <= c-1:
        visited[r][c-1] = 1
        queue.append((time+1, r, c-1))
    if c+K < N+K and time+1 <= c+K:
        if r == 0 and not visited[1][c+K] and A[1][c+K]:
            visited[1][c+K] = 1
            queue.append((time+1, 1, c+K))
        if r == 1 and not visited[0][c+K] and A[0][c+K]:
            visited[0][c+K] = 1
            queue.append((time+1, 0, c+K))
else: print(0)