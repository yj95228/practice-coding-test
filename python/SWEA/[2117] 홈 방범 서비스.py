# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu
from collections import deque

def check(x, y):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    queue = deque([(x, y)])
    k, result, answer = 1, 0, 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if matrix[r][c] == 1: result += 1
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        if M*result-(k**2+(k-1)**2) >= 0:
            answer = max(answer, result)
        k += 1
    return answer

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            answer = max(answer, check(r, c))
    print(f'#{tc} {answer}')