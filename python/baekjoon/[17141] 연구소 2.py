'''
- 바이러스 안 놓는 칸도 빈 칸으로 침
- 1차. 95% 틀렸습니다
- 2차. 바이러스 놓고 퍼뜨리는데 시간이 안 드는 경우를 고려하여 종료조건을 앞에 두기
'''
from sys import stdin
from collections import deque
input = stdin.readline

def recur(n, start, arr):
    global answer
    if n == M:
        result = safe-M
        queue = deque(arr)
        visited = [[False]*N for _ in range(N)]
        for r, c in arr:
            visited[r][c] = True
        time = 0
        while queue:
            if not result:
                answer = min(answer, time)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and matrix[nx][ny] != '1':
                        result -= 1
                        visited[nx][ny] = True
                        queue.append((nx,ny))
            time += 1
        return
    for i in range(start, length):
        recur(n+1, i+1, arr+[virus[i]])

N, M = map(int, input().split())
matrix = [input().split() for _ in range(N)]
safe, virus = 0, []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == '2':
            virus.append((r,c))
            safe += 1
        elif matrix[r][c] == '0':
            safe += 1
length = len(virus)
answer = N*N+1
recur(0,0,[])
print(-1 if answer == N*N+1 else answer)