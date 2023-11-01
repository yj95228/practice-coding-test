from sys import stdin
from collections import deque
input = stdin.readline

N, M, P = map(int, input().split())
S = list(map(int, input().split()))
matrix = [list(input().rstrip()) for _ in range(N)]
castle = [[] for _ in range(P)]
cnt = [0]*P
for r in range(N):
    for c in range(M):
        if matrix[r][c].isdigit():
            num = int(matrix[r][c])-1
            matrix[r][c] = num+1
            castle[num].append((r, c))
            cnt[num] += 1

while True:
    new_castle = [[] for _ in range(P)]
    for p in range(P):
        queue = deque(castle[p])
        temp_q = []
        for s in range(S[p]):
            if not queue: break
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '.':
                        matrix[nx][ny] = p+1
                        cnt[p] += 1
                        new_castle[p].append((nx, ny))
                        queue.append((nx, ny))
                        if s+1 == S[p]: temp_q.append((nx, ny))
        new_castle[p] = temp_q
    if not sum(map(len, new_castle)): break
    castle = new_castle
print(*cnt)